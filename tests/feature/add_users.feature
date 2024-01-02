Feature: AddUsers
  # Add users with assorted combinations

  Scenario: Add Basic User
    When The following is posted to the "add-users" endpoint using PUT
    """
    [
        {
            "name": "Jorge",
            "email": "jorge.professional@outlook.com",
            "phone": "(443)802-5076",
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
        },
        {
            "name": "Julieta",
            "email": "julieta.professional@outlook.com",
            "phone": "(443)630-5126",
            "skills": [
                {
                    "name": "BioTech",
                    "level": 3
                },
                {
                    "name": "French",
                    "level": 2
                }
            ]
        }
    ]
    """
    Then response should be
    """
    [1, 2]
    """

  Scenario: Add Incorrect User Data
    When The following is posted to the "add-users" endpoint using PUT
    """
    {
        "name": "Jorge",
        "email": "jcardenas.professional@outlook.com"
    }
    """
    Then api should fail
