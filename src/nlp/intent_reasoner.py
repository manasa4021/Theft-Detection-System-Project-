def decide_intent(actions,
                  min_frames=25,
                  min_suspicious=8,
                  min_ratio=0.25):
    """
    Balanced thresholds to detect theft
    without causing early false alarms.
    """

    if len(actions) < min_frames:
        return "normal", "Not enough evidence for suspicious behavior."

    total = len(actions)
    suspicious = actions.count("hand_near_pocket")
    ratio = suspicious / total

    if suspicious >= min_suspicious and ratio >= min_ratio:
        return (
            "theft_suspected",
            f"Theft-like activity detected "
            f"({suspicious}/{total} suspicious frames, ratio={ratio:.2f})"
        )

    return (
        "normal",
        f"Behavior appears normal "
        f"({suspicious}/{total} suspicious frames, ratio={ratio:.2f})"
    )
