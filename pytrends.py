import pytrends

def get_high_demand_titles():
  """This function gets the high demand titles from Google Trends.

  Returns:
    A list of high demand titles.
  """

  pytrends = pytrends.GoogleTrends()
  high_demand_titles = pytrends.get_high_demand_titles()

  return high_demand_titles
