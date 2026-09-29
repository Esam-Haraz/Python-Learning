gamer_profile = {
    "name": "Osama",
    "level": 99,
    "achievements": [
        {"title": "First Win", "score": 100},
        {"title": "Pro Player", "score": 5000}
    ],
    "settings": {
        "audio": {
            "music": 50, 
            "sfx": 100
        },
        "video": "Ultra"
    }
}
print(f"Pro Player Score: {gamer_profile['achievements'][1]["score"]}")
print(f"SFX Volume: {gamer_profile['settings']['audio']["sfx"]}")
gamer_profile["settings"]['video'] = "Low"
gamer_profile["achievements"].append({"title": "Legend", "score": 10000})
print(gamer_profile)
