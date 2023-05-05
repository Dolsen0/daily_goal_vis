import matplotlib.pyplot as plt
import pandas as pd
from plan import df



# Create pie chart
plt.pie(df['duration'], labels=df['title'], autopct='%1.1f%%')

# Add title to chart
plt.title('Daily Goal')

# Display the chart
plt.show()