Feature: AddUsers
  # Add users with assorted combinations

  Scenario: Add Basic User
    When The following is posted to the "add-users" endpoint using PUT
    """
    {
        "name": "Jorge",
        "email": "jcardenas.professional@outlook.com",
        "phone": "(443)802-5076"
    }
    """
    Then response should be
    """
    {
      "name": "Jorge",
      "email": "jcardenas.professional@outlook.com",
      "id": 1
    }
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
