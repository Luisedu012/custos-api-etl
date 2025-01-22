import requests

def fetch_depreciation_data(year=None, month=None, legal_nature=None, org_level_1=None, org_level_2=None, org_level_3=None):
    """
    Fetches depreciation, amortization, and exhaustion cost data from the API.

    Parameters:
        year (int): Year of the accounting entry.
        month (int): Month of the accounting entry (1 to 12).
        legal_nature (int): Legal nature of the organization.
        org_level_1 (str): Organizational unit at the ministry/AGU level (SIORG code).
        org_level_2 (str): Organizational unit one level below the ministry/AGU level (SIORG code).
        org_level_3 (str): Organizational unit two levels below the ministry/AGU level (SIORG code).

    Returns:
        dict: JSON response from the API.
    """
    url = "https://apidatalake.tesouro.gov.br/ords/custos/tt/depreciacao"

    # Query parameters
    params = {
        "ano": year,
        "mes": month,
        "natureza_juridica": legal_nature,
        "organizacao_n1": org_level_1,
        "organizacao_n2": org_level_2,
        "organizacao_n3": org_level_3,
    }

    try:
        # Make the GET request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
data = fetch_depreciation_data(year=2023, month=1)

if data:
    print("API Response:")
    print(data)
