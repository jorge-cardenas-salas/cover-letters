Feature: AddUsers
  # Add users with assorted combinations

  Scenario: Add Basic User
    When The following is posted to the "add-users" endpoint
    """
    {
        "id": 1,
        "name": "Jorge",
        "email": "jcardenas.professional@outlook.com",
        "skills": [
            {
                "name": "Python",
                "level": 3
            },
            {
                "name": "SQL",
                "level": 3
            }
        ]
    }
    """
    Then Dummy Success
