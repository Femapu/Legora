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
