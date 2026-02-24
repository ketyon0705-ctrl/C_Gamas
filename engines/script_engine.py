def generate_script(topic):
    """
    Mock Script Engine.
    Returns a list of strings representing the script parts.
    """
    if "cats" in topic.lower():
        return [
            "Why do cats love boxes so much?",
            "It gives them a sense of security and safety from predators.",
            "Also, it's just really fun to hide in them!"
        ]
    else:
        return [
            f"Here is a video about {topic}.",
            "This is the first generated sentence.",
            "And this is the final conclusion."
        ]
