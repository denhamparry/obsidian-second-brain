"""Regression tests for the concise skill router and concurrent-write contract."""

from __future__ import annotations

import ast
import re
from collections.abc import Callable
from pathlib import Path
from threading import Lock

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = REPO_ROOT / "SKILL.md"
ROUTING_PATH = REPO_ROOT / "references/command-routing.md"
FOCUSED_REFERENCES = tuple(
    REPO_ROOT / "references" / name
    for name in (
        "command-routing.md",
        "hooks-and-project-vaults.md",
        "knowledge-maintenance.md",
        "research-operations.md",
        "scheduled-agents.md",
        "vault-setup.md",
        "work-session-updates.md",
    )
)
COMMAND_LINK = re.compile(r"\]\(\.\./commands/([a-z0-9-]+)\.md\)")
ROUTE_ROW = re.compile(
    r"^\| `/([a-z0-9-]+)` \| (.*?) \| \[`commands/[^`]+`\]", re.MULTILINE
)
TRIGGERS_LINE = re.compile(r"^triggers_en: (\[.*\])$", re.MULTILINE)
LOCAL_LINK = re.compile(r"\]\((?!https?://|#)([^)#]+\.md)(?:#[^)]+)?\)")


class ConcurrentUpdateError(RuntimeError):
    """The target kept changing before a conditional mutation could land."""


class AppendOnlyViolation(RuntimeError):
    """A proposed operation-log update did not preserve its prior prefix."""


class ConditionalTextFile:
    """Cooperative file adapter with atomic compare-and-mutate primitives."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._lock = Lock()

    def read(self) -> str:
        with self._lock:
            return self.path.read_text(encoding="utf-8")

    def append(self, addition: str) -> None:
        with self._lock, self.path.open("a", encoding="utf-8") as stream:
            stream.write(addition)

    def replace_if_unchanged(self, expected: str, updated: str) -> bool:
        with self._lock:
            if self.path.read_text(encoding="utf-8") != expected:
                return False
            self.path.write_text(updated, encoding="utf-8")
            return True

    def append_if_unchanged(self, expected: str, addition: str) -> bool:
        with self._lock:
            if self.path.read_text(encoding="utf-8") != expected:
                return False
            with self.path.open("a", encoding="utf-8") as stream:
                stream.write(addition)
            return True


def apply_optimistic_update(
    target: ConditionalTextFile,
    build_update: Callable[[str], str],
    *,
    before_mutation: Callable[[int, ConditionalTextFile], None] | None = None,
    after_mutation: Callable[[int, ConditionalTextFile], None] | None = None,
    append_only: bool = False,
    max_attempts: int = 3,
) -> int:
    """Model reread plus an atomic conditional mutation and bounded retries."""

    for attempt in range(1, max_attempts + 1):
        current = target.read()
        updated = build_update(current)
        if append_only and not updated.startswith(current):
            raise AppendOnlyViolation(f"append-only update would rewrite {target.path}")

        if before_mutation is not None:
            before_mutation(attempt, target)

        if append_only:
            committed = target.append_if_unchanged(current, updated[len(current) :])
        else:
            committed = target.replace_if_unchanged(current, updated)
        if not committed:
            continue

        if after_mutation is not None:
            after_mutation(attempt, target)

        verified = target.read()
        if append_only and verified.startswith(updated):
            return attempt
        if not append_only and verified == updated:
            return attempt
        if not append_only:
            continue

    raise ConcurrentUpdateError(
        f"unresolved concurrent update for {target.path} after {max_attempts} attempts"
    )


def _append_once(content: str, addition: str) -> str:
    if addition in content:
        return content
    return content + addition


def test_top_level_skill_is_a_small_router():
    text = SKILL_PATH.read_text(encoding="utf-8")

    assert len(text.splitlines()) < 220
    assert "## Research Commands" not in text
    assert "## Scheduled Agents" not in text
    assert "references/work-session-updates.md" in text
    assert "references/command-routing.md" in text
    assert "references/knowledge-maintenance.md" in text



@pytest.mark.parametrize("source", (SKILL_PATH, *FOCUSED_REFERENCES))
def test_router_reference_links_resolve(source: Path):
    for relative in LOCAL_LINK.findall(source.read_text(encoding="utf-8")):
        target = (source.parent / relative).resolve()
        assert target.is_file(), f"{source.relative_to(REPO_ROOT)} -> {relative}"


def test_command_router_maps_every_command_exactly_once():
    routing_text = ROUTING_PATH.read_text(encoding="utf-8")
    routes = COMMAND_LINK.findall(routing_text)
    command_names = sorted(path.stem for path in (REPO_ROOT / "commands").glob("*.md"))

    assert len(routes) == len(set(routes)), "duplicate canonical command route"
    assert sorted(routes) == command_names
    assert len(routes) == 44

    route_triggers = {
        command: [trigger.strip() for trigger in triggers.split(";")]
        for command, triggers in ROUTE_ROW.findall(routing_text)
    }
    assert sorted(route_triggers) == command_names
    all_triggers = [trigger.casefold() for triggers in route_triggers.values() for trigger in triggers]
    assert len(all_triggers) == len(set(all_triggers)), "duplicate natural-language trigger"

    for command in command_names:
        command_text = (REPO_ROOT / "commands" / f"{command}.md").read_text(
            encoding="utf-8"
        )
        match = TRIGGERS_LINE.search(command_text)
        assert match is not None, command
        assert route_triggers[command] == ast.literal_eval(match.group(1)), command


def test_routine_work_session_reference_is_self_contained():
    text = (REPO_ROOT / "references/work-session-updates.md").read_text(encoding="utf-8")

    assert "Reread, merge, and retry" in text
    assert "Append-only operation logs" in text
    assert "research-operations.md" not in text
    assert "scheduled-agents.md" not in text
    assert "hooks-and-project-vaults.md" not in text


def test_interleaved_write_retries_and_preserves_both_updates(tmp_path: Path):
    path = tmp_path / "daily.md"
    path.write_text("# Daily\n\n- Existing\n", encoding="utf-8")
    daily = ConditionalTextFile(path)

    def concurrent_writer(attempt: int, target: ConditionalTextFile) -> None:
        if attempt == 1:
            target.append("- Concurrent entry\n")

    attempts = apply_optimistic_update(
        daily,
        lambda current: _append_once(current, "- Requested update\n"),
        before_mutation=concurrent_writer,
    )

    assert attempts == 2
    assert daily.read() == (
        "# Daily\n\n- Existing\n- Concurrent entry\n- Requested update\n"
    )


def test_append_only_log_preserves_concurrent_entry_and_prior_prefix(tmp_path: Path):
    path = tmp_path / "log.md"
    original = "## 2026-09-05\n- Existing operation\n"
    path.write_text(original, encoding="utf-8")
    operation_log = ConditionalTextFile(path)

    def concurrent_writer(attempt: int, target: ConditionalTextFile) -> None:
        if attempt == 1:
            target.append("- Concurrent operation\n")

    attempts = apply_optimistic_update(
        operation_log,
        lambda current: _append_once(current, "- Requested operation\n"),
        before_mutation=concurrent_writer,
        append_only=True,
    )
    result = operation_log.read()

    assert attempts == 2
    assert result.startswith(original)
    assert result.endswith("- Concurrent operation\n- Requested operation\n")


def test_append_only_post_commit_interleave_is_exactly_once(tmp_path: Path):
    path = tmp_path / "log.md"
    path.write_text("- Existing operation\n", encoding="utf-8")
    operation_log = ConditionalTextFile(path)

    def post_commit_writer(attempt: int, target: ConditionalTextFile) -> None:
        if attempt == 1:
            target.append("- Concurrent operation after commit\n")

    attempts = apply_optimistic_update(
        operation_log,
        lambda current: _append_once(current, "- Requested operation\n"),
        after_mutation=post_commit_writer,
        append_only=True,
    )
    result = operation_log.read()

    assert attempts == 1
    assert result.count("- Requested operation\n") == 1
    assert result.endswith(
        "- Requested operation\n- Concurrent operation after commit\n"
    )


def test_append_only_log_rejects_rewrite(tmp_path: Path):
    path = tmp_path / "log.md"
    path.write_text("- Existing operation\n", encoding="utf-8")
    operation_log = ConditionalTextFile(path)

    with pytest.raises(AppendOnlyViolation, match="append-only update would rewrite"):
        apply_optimistic_update(
            operation_log,
            lambda _current: "- Replacement operation\n",
            append_only=True,
        )

    assert operation_log.read() == "- Existing operation\n"


def test_repeated_conflicts_stop_after_three_attempts(tmp_path: Path):
    path = tmp_path / "project.md"
    path.write_text("# Project\n", encoding="utf-8")
    project = ConditionalTextFile(path)

    def persistent_writer(attempt: int, target: ConditionalTextFile) -> None:
        target.append(f"- Concurrent {attempt}\n")

    with pytest.raises(
        ConcurrentUpdateError,
        match=r"unresolved concurrent update .* after 3 attempts",
    ):
        apply_optimistic_update(
            project,
            lambda current: current + "- Requested update\n",
            before_mutation=persistent_writer,
        )

    result = project.read()
    assert "- Concurrent 1\n" in result
    assert "- Concurrent 2\n" in result
    assert "- Concurrent 3\n" in result
    assert "- Requested update\n" not in result
