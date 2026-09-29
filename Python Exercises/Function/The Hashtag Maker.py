make_hashtag = lambda text: f"Your Hashtag is #{text.strip().lower().replace(" ", "-")}"
print(make_hashtag("   PyThOn Is Awesome    "))
