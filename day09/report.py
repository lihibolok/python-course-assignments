# day09/report.py

"""
Day 09 assignment report

This script reads:
- day09/subjects.txt (issues from the shared course repository)

and uses hard-coded deadlines that were taken from the teacher's main README
(so we don't need to parse your own README.md).

It then creates a simple, useful report with:
1. The deadlines used.
2. Popularity of each assignment (how many issues, and OPEN vs CLOSED).
3. On-time vs late submissions for each assignment (where we have a deadline).
4. A short list of late submissions (first 30), with how many days late.

Output is printed to the terminal and also saved to day09/report.txt.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import re


# -------------------------------------------------------------------
#  Hard-coded deadlines (copied from the teacher's course README)
# -------------------------------------------------------------------
# Dates are in the format: YYYY, MM, DD, HH, MM  (local course time)
DEADLINES: dict[str, datetime] = {
    "Day01": datetime(2025, 11, 2, 22, 0),   # Amendment deadline used
    "Day02": datetime(2025, 11, 9, 22, 0),
    "Day03": datetime(2025, 11, 16, 22, 0),
    "Day04": datetime(2025, 11, 23, 22, 0),
    "Day05": datetime(2025, 11, 29, 22, 0),
    "Day06": datetime(2025, 12, 6, 22, 0),
    # README does not define a separate deadline for Day07
    "Day08": datetime(2025, 12, 30, 22, 0),
    "Day09": datetime(2026, 1, 10, 22, 0),
    "Project proposal": datetime(2026, 1, 11, 22, 0),
    "Project submission": datetime(2026, 1, 25, 22, 0),
}


# -------------------------------------------------------------------
#  Data structure for one submission (one issue)
# -------------------------------------------------------------------

@dataclass
class Submission:
    issue_id: int
    status: str           # "OPEN" or "CLOSED"
    subject: str          # full subject line
    timestamp: datetime   # issue creation time (UTC from the file)
    assignment: str | None  # e.g. "Day02", "Project proposal", or None
    student: str | None     # student name if we can extract it


# -------------------------------------------------------------------
#  Parsing day09/subjects.txt
# -------------------------------------------------------------------

# The lines we care about look like:
#  213    OPEN    Day08 by Shoshana Sernik        2026-01-03T18:44:38Z
ISSUE_LINE_PATTERN = re.compile(
    r"^\s*(\d+)\s+([A-Z]+)\s+(.+?)\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s*$"
)


def extract_assignment(subject: str) -> str | None:
    """
    Try to infer which assignment an issue belongs to based on the subject.

    Handles things like:
      - "Day08 by Someone"
      - "day 05 by Someone"
      - "Final Project proposal by Someone"
      - "day 08 and proposal for final project-Name"
    """
    s_lower = subject.lower()

    # Project-related issues first
    if "final project" in s_lower and "proposal" in s_lower:
        return "Project proposal"
    if "final project" in s_lower and "submission" in s_lower:
        return "Project submission"

    # Any "day XX" variant, e.g.:
    #   "Day1", "Day 1", "day01", "day 05", etc.
    m = re.search(r"day\s*0?(\d+)", s_lower)
    if m:
        day = int(m.group(1))
        return f"Day{day:02d}"

    return None


def extract_student(subject: str) -> str | None:
    """
    Extract the student name from the subject line.

    We mostly rely on the pattern "by <Name>", e.g.:
        "Day08 by Lihi Bolokan" -> "Lihi Bolokan"

    As a fallback, if there is a hyphen in the subject, we take the part
    after the first "-" as the "name".
    """
    # Try to find 'by <Name>'
    m = re.search(r"\bby\b(.+)$", subject, re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # Fallback: split on "-" and take the right side
    if "-" in subject:
        return subject.split("-", maxsplit=1)[1].strip()

    return None


def parse_subjects(subjects_path: Path) -> list[Submission]:
    """
    Parse the subjects.txt file into a list of Submission objects.
    """
    submissions: list[Submission] = []

    for raw_line in subjects_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        m = ISSUE_LINE_PATTERN.match(line)
        if not m:
            # skip lines that don't match the expected pattern
            continue

        issue_id = int(m.group(1))
        status = m.group(2)
        subject = m.group(3)
        timestamp_str = m.group(4)

        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")

        assignment = extract_assignment(subject)
        student = extract_student(subject)

        submissions.append(
            Submission(
                issue_id=issue_id,
                status=status,
                subject=subject,
                timestamp=timestamp,
                assignment=assignment,
                student=student,
            )
        )

    return submissions


# -------------------------------------------------------------------
#  Building simple statistics from the submissions
# -------------------------------------------------------------------

def build_reports(submissions: list[Submission]):
    """
    From the parsed submissions, compute:
    - popularity: how many issues per assignment
    - status_counts: OPEN vs CLOSED per assignment
    - timing_stats: on-time vs late (only for assignments with deadlines)
    - late_submissions: list of (Submission, delay) tuples
    """
    popularity = Counter()                    # assignment -> total count
    status_counts = defaultdict(Counter)      # assignment -> {status -> count}
    timing_stats: dict[str, dict[str, int]] = {}
    late_submissions: list[tuple[Submission, datetime]] = []

    for sub in submissions:
        tag = sub.assignment or "Other"

        # Popularity and status distribution
        popularity[tag] += 1
        status_counts[tag][sub.status] += 1

        # On-time vs late: only if we have a deadline
        if sub.assignment not in DEADLINES:
            continue

        deadline = DEADLINES[sub.assignment]
        stats = timing_stats.setdefault(
            sub.assignment, {"total": 0, "on_time": 0, "late": 0}
        )
        stats["total"] += 1

        if sub.timestamp <= deadline:
            stats["on_time"] += 1
        else:
            stats["late"] += 1
            late_submissions.append((sub, sub.timestamp - deadline))

    return popularity, status_counts, timing_stats, late_submissions


def format_report(
    popularity: Counter,
    status_counts: dict[str, Counter],
    timing_stats: dict[str, dict[str, int]],
    late_submissions: list[tuple[Submission, datetime]],
) -> str:
    """
    Turn all the computed information into a human-readable text report.
    """
    lines: list[str] = []

    # 1. Show the deadlines we used
    lines.append("=== Deadlines used ===")
    for tag, dt in DEADLINES.items():
        lines.append(f"{tag:>18}: {dt.isoformat(' ')}")
    lines.append("")

    # 2. Popularity of each assignment
    lines.append("=== Popularity of assignments (number of issues) ===")
    for tag, count in popularity.most_common():
        counts = status_counts[tag]
        status_str = ", ".join(f"{status}: {n}" for status, n in sorted(counts.items()))
        lines.append(f"{tag:>18}: {count:3d} issues ({status_str})")
    lines.append("")

    # 3. On-time vs late statistics
    lines.append("=== On-time vs late submissions (based on issue creation time) ===")
    for tag in sorted(timing_stats.keys()):
        stats = timing_stats[tag]
        lines.append(
            f"{tag:>18}: total={stats['total']:3d}, "
            f"on time={stats['on_time']:3d}, late={stats['late']:3d}"
        )
    lines.append("")

    # 4. List a few late submissions
    lines.append("=== Late submissions (first 30, sorted by smallest delay) ===")
    late_sorted = sorted(late_submissions, key=lambda item: item[1])
    for sub, delay in late_sorted[:30]:
        days_late = delay.total_seconds() / 86400.0
        student = sub.student or "Unknown student"
        tag = sub.assignment or "Unknown assignment"
        lines.append(
            f"#{sub.issue_id:3d} {tag:>10} by {student:25s}: "
            f"{sub.timestamp.isoformat()} ({days_late:5.2f} days late)"
        )

    return "\n".join(lines)


# -------------------------------------------------------------------
#  Main entry point
# -------------------------------------------------------------------

def main() -> None:
    this_dir = Path(__file__).resolve().parent
    subjects_path = this_dir / "subjects.txt"

    if not subjects_path.exists():
        raise SystemExit(f"Could not find subjects.txt at {subjects_path}")

    submissions = parse_subjects(subjects_path)
    popularity, status_counts, timing_stats, late_submissions = build_reports(
        submissions
    )

    report_text = format_report(
        popularity, status_counts, timing_stats, late_submissions
    )

    # Print to screen
    print(report_text)

    # Also save to day09/report.txt
    output_path = this_dir / "report.txt"
    output_path.write_text(report_text, encoding="utf-8")
    print(f"\nReport written to: {output_path}")


if __name__ == "__main__":
    main()
