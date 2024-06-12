# Sea Level Predictor

Instructions for building this project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor

## Comments on Tests

My original code is more concise and produces the correct lines.
```
# Create first line of best fit
line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
ax.axline(xy1=(0, line1.intercept), slope=line1.slope, color='r')

# Create second line of best fit
line2 = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
ax.axline(xy1=(0, line2.intercept), slope=line2.slope, color='g')
```

However, this code will fail the given tests as they check for the list of values used in plotting (https://forum.freecodecamp.org/t/attributeerror-list-object-has-no-attribute-tolist-sea-level-predictor/598500/5). To circumvent this, the code needs to calculate the predicted values for each year, as seen in the final result.
