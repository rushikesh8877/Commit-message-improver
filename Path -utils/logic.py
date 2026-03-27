def improve_commit(msg):
    msg = msg.strip().lower()

    if "fix" in msg:
        return f"fix(core): {msg}"

    elif "add" in msg or "feature" in msg:
        return f"feat(core): {msg}"

    elif "doc" in msg:
        return f"docs: {msg}"

    elif "refactor" in msg:
        return f"refactor: {msg}"

    else:
        return f"chore: {msg}"
