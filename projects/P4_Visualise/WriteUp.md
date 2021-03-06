# Create a Tableau Story

## Introduction

The goal of this project is to create an explanatory data visualization from a data set that communicates a clear finding or that highlights relationships or patterns in the data.

The final tableau story can be found here.
https://public.tableau.com/profile/tim.franken#!/vizhome/baseball_v2_0/Story1

The initial story can be found here:
https://public.tableau.com/profile/tim.franken#!/vizhome/init_P4_baseball/Dashboard1

## Summary
The data set used in this project contains information about 1157 baseball players including their handedness (right or left handed), height (in inches), batting average, and home runs. The performance indicators home runs and batting average show a high variations. This variance can be partly explained by handedness for home runs and height for batting average.

## Design
After an initial data exploration phase it became clear that the handedness has a significant impact on the average number of homeruns while the height mainly impacts the batting average. This is the main message I wanted to convey in the explanatory visualisation.

The visualisation should therefore show the evolution of:

* Average homeruns in function of handedness
* Average batting average in function of height

However as a researcher I would also be interested to see if the height has no influence in the average number of homeruns or if the handedness has no influence on the batting average. Therefore I choose to show these as well in the graphs. I choose for bar charts in both cases to get a uniform dashboard. The bar chart was choosen since it is the most simple and clear visualisation for categorical data. The charts were kept plain and simple with labels on top of the bar charts to give a clear overview. All other chart junk was removed. No colors have been used to distinguish between the categories in the bar chart as this would only distract from the data and the message. Labels on the axis were converted to human understable information. I have not removed the y-axis since I still want to see them there from a scientific point of view.

After the feedback I altered some of the initial design choices:

* Adapted the chart type for performance in function of height.
* In order to distinguish my main message I adapted the visualisation to show different colors that emphasize the main conclusions. A light blue color was choosen as it is a soft color that does not distract the reader but still draws the attention to the focus point of the graphs.
* Adapted the tooltips to get human readable values.

Additionally  one more introductory page was added at the beginning of the story after the feedback round that illustrated the variation in batting average and homeruns. Boxplots were choosen here as they are a visually effective way of viewing a summary of your data.

## Feedback

I posted the first version of my visualisations on our company Yammer platform in order to receive feedback. I received three comments on the post. 

> Height is a continuous variable so the bar charts are rather contra-intuitive. 

I agreed with the feedback and adapted the chart type for performance in function of height.

> The main message is not very clear yet since different charts are provided. It takes some time to link the explanation in the captions to the graphs.

 In order to distinguish my main message I therefore adapted the visualisation to show different colors that emphasize the main conclusions.
 
 > The text in the tooltips is not human readable.
 
 This is something I did not check prior to publishing the first version but I adapted it after the comments.
 
 > The labels from the chart of height in function of batting average are overcrowding the graph
 
The labels have been deleted from the graph since I opted for a different chart type here.
 
  
## Resources

Data was downloaded from:
https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud507/baseball_data.csv&sa=D&ust=1516290329579000&usg=AFQjCNFoi0DgIU4e7LUEgzxMs-sTIjgYWg