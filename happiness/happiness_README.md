# Analysis Report

### Analysis Story: Global Wellbeing Metrics and their Correlations

#### Dataset Overview
This dataset encompasses a comprehensive study of global wellbeing metrics across 2363 entries spanning 165 countries from 2005 to 2023. Key indicators include:

- **Life Ladder**: A measure of subjective wellbeing.
- **Log GDP per capita**: A log transformation of GDP per capita, a commonly used economic indicator.
- **Social Support**: Reflecting individuals' perceptions of assistance from family and friends.
- **Healthy Life Expectancy at Birth**: An indicator of health coupled with life expectancy.
- **Freedom to Make Life Choices**: A measure of personal agency.
- **Generosity**: Captured as a measure of charitable behavior.
- **Perceptions of Corruption**: A gauge of public trust and governance.
- **Positive and Negative Affect**: Emotional wellbeing indicators.

#### Insights

1. **Overall Wellbeing**:
   - The mean Life Ladder score of approximately **5.48** indicates a moderate level of subjective wellbeing. The standard deviation of **1.13** suggests variability among countries, with some achieving significantly higher scores.
   - The maximum Life Ladder score of **8.02** highlights countries where citizens report very high wellbeing levels.

2. **Economic Indicators**:
   - There exists a strong positive correlation (**0.77**) between Life Ladder and Log GDP per capita. This reflects that as economic prosperity increases, so does subjective wellbeing. 
   - Countries with higher GDP per capita also tend to have higher scores in other wellbeing metrics such as Healthy Life Expectancy (correlation **0.81**).

3. **Social Support and Wellbeing**:
   - A notable correlation of **0.72** exists between Social Support and Life Ladder scores. This suggests that robust social networks significantly contribute to perceived wellbeing.
   - The associated importance of social connections highlights that policies fostering social cohesion could enhance wellbeing.

4. **Health Outcomes**:
   - Healthy life expectancy at birth correlates with Life Ladder scores (**0.71**), indicating that better health contributes to higher wellbeing perceptions.
   - Investment in healthcare and public health strategies could, therefore, promote higher wellbeing scores.

5. **Freedom and Corruption**:
   - Freedom to make life choices correlates positively with Life Ladder (**0.54**), suggesting societies that support personal agency and freedom tend to report higher wellbeing.
   - Conversely, perceptions of corruption correlate negatively with Life Ladder scores (**-0.42**). Higher corruption perceptions can erode trust in institutions and harm subjective wellbeing.

6. **Affective Wellbeing**:
   - There’s a positive correlation between positive affect and Life Ladder (**0.51**) and a negative correlation with negative affect (**-0.35**). This underscores that emotional states significantly impact how individuals rate their wellbeing.

#### Implications

- **Policy Recommendations**:
  - Governments should prioritize economic growth alongside equitable wealth distribution to elevate overall subjective wellbeing.
  - Social policies aimed at enhancing community engagement and support networks are essential for fostering social support.
  - Public health initiatives that focus on improving life expectancy and quality of life can yield significant benefits in terms of societal happiness.
  - Enhancing personal freedoms and reducing corruption may lead to a higher level of trust and satisfaction among citizens.

- **Areas for Further Research**:
  - More granular analysis is required to understand the cultural contexts behind wellbeing in various countries.
  - Exploring the impact of specific policies on wellbeing metrics could provide actionable insights for governments.

- **International Comparison**:
  - Countries like Lebanon, which appear frequently in the dataset, should be examined for patterns and unique insights, especially since it tops in frequency.

#### Conclusion

This dataset presents a valuable resource for understanding the complexities of wellbeing worldwide. The insights gleaned can guide policymakers and stakeholders in formulating strategies that not only boost economic indicators but also enhance the psychological and social fabric of society. By fostering environments that prioritize health, freedom, and social support, countries can work towards elevating the overall wellbeing of their citizens.

![Correlation Heatmap](goodreads_correlation_heatmap.png)
![col1 Histogram](happiness_col1_histogram.png)
![col2 Histogram](happiness_col2_histogram.png)
![col3 Histogram](happiness_col3_histogram.png)
