pidgey = {"name": "Pidgey",
          "attacks": {
                        "peck": {"name": "PECK", "power": 5, "acc": 3},
                        "gust": {"name": "GUST", "power": 4, "acc": 4}
                      },
            "type": "flying"
                      }

print(pidgey["attacks"])
print(pidgey.get("attacks"))