#!/usr/bin/env python3
"""Push the day's drafts to the LegoraBot Discord inbox. Author: Stefano Puddu.

Usage:
  python3 push_discord.py drafts.json "<webhook url>" <slot id> [<slot id> ...]
  python3 push_discord.py --create "<webhook url>" [count]   # creates empty slots once

drafts.json: {"drafts": [{"id", "day", "flair", "title", "body"}, ...]}
Each draft goes into one slot message as an embed. Slots not used today are
reset to a placeholder, so old drafts are never imported twice (the bot also
remembers imported ids).
"""
import json
import sys
import urllib.request

UA = "LegoraBot drafts (Claude)"


def call(method, url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read()
        return json.loads(body) if body else {}


def base(webhook):
    return webhook.strip().rstrip("/").split("?")[0]


def placeholder():
    return {"content": "Empty slot (no draft).", "embeds": []}


def embed(d):
    meta = {"id": d["id"], "day": d["day"], "flair": d.get("flair", "Bot")}
    title, body = d["title"].strip(), d["body"].strip()
    if "—" in title + body:
        sys.exit(f"Draft {d['id']} contains an em dash")
    if len(title) > 256:
        sys.exit(f"Title too long for Discord ({len(title)} > 256): {d['id']}")
    if not 200 <= len(body) <= 4096:
        sys.exit(f"Body must be 200-4096 characters for Discord ({len(body)}): {d['id']}")
    return {"title": title, "description": body, "footer": {"text": json.dumps(meta)}}


def main():
    if sys.argv[1] == "--create":
        hook = base(sys.argv[2])
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 2
        ids = [call("POST", hook + "?wait=true", placeholder())["id"] for _ in range(n)]
        print("SETTING:", hook, " ".join(ids))
        return
    drafts = json.load(open(sys.argv[1]))["drafts"]
    hook, slots = base(sys.argv[2]), sys.argv[3:]
    if len(drafts) > len(slots):
        sys.exit(f"{len(drafts)} drafts but only {len(slots)} slots")
    for i, slot in enumerate(slots):
        if i < len(drafts):
            d = drafts[i]
            payload = {"content": f"Draft {d['id']}", "embeds": [embed(d)]}
        else:
            payload = placeholder()
        call("PATCH", f"{hook}/messages/{slot}", payload)
    # verify
    for i, d in enumerate(drafts):
        got = call("GET", f"{hook}/messages/{slots[i]}")
        meta = json.loads(got["embeds"][0]["footer"]["text"])
        assert meta["id"] == d["id"], "verification failed"
        print("OK", slots[i], d["id"])


if __name__ == "__main__":
    main()
