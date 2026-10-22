# r/Legora drafts

Author: Stefano Puddu.

Draft posts for r/Legora, an unofficial community about Legora and legal AI. Drafts are written each morning by Claude and picked up by the LegoraBot app, where a human moderator reviews them before publication.

Not affiliated with or endorsed by Legora.

## Format of `inbox.json`

```json
{
  "drafts": [
    {
      "id": "2026-10-23-spotlight-agent",
      "day": "2026-10-23",
      "flair": "Legora Spotlight",
      "title": "Legora Spotlight: the Legora Agent",
      "body": "Markdown body, at least 200 characters"
    }
  ]
}
```

- `id`: unique, letters, numbers, `-` or `_`, 6 to 80 characters. Start with the date.
- `day`: publication day (YYYY-MM-DD). Drafts older than two days are ignored.
- `flair`: one of Bot, News, Discussion, Prompt, Workflow, Legora Spotlight, Meta.
- Keep only the last 14 drafts in the file.

## `history.json`: what has already been covered

Permanent log of every draft, never truncated. Read it before writing a new draft to avoid repeating content.

```json
{"entries": [{"day": "2026-10-22", "format": "Legora Spotlight", "topic": "Legora Agent", "title": "...", "links": ["https://..."]}]}
```

Rules for new drafts:

- Legora Spotlight: no feature repeated within 8 weeks.
- Prompt Tuesday, Question of the Week, Show Your Workflow: no topic repeated within 12 weeks.
- News and digest items: never reuse a link already in the log.
- Evergreen posts: never repeat a topic.
