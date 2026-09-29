default_settings = {
    "volume": 50,
    "resolution": "1080p",
    "difficulty": "Normal",
    "subtitles": True
}

user_customization = {
    "volume": 80,        
    "difficulty": "Hard" 
}
default_settings.update(user_customization)
print(default_settings)