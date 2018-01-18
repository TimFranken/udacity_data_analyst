# Create a Tableau Story

## Introduction

The goal of this project is to create an explanatory data visualization from a data set that communicates a clear finding or that highlights relationships or patterns in the data.

The final tableau story can be found here.
https://public.tableau.com/profile/tim.franken#!/vizhome/baseball_11/Dashboard1

The initial story can be found here:
https://public.tableau.com/profile/tim.franken#!/vizhome/init_P4_baseball/Dashboard1

## Summary
The data set used in this project contains information about 1157 baseball players including their handedness (right or left handed), height (in inches), batting average, and home runs. The performance indicators (home runs and batting average) show significant differences in function of respectively handedness and height.

## Design
After an initial data exploration phase it became clear that the handedness has a significant impact on the average number of homeruns while the height mainly impacts the batting average. This is the main message I wanted to convey in the explanatory visualisation.

The visualisation should therefore show the evolution of:

* Average homeruns in function of handedness
* Average batting average in function of height

However as a researcher I would also be interested to see if the height has no influence in the average number of homeruns or if the handedness has no influence on the batting average. Therefore I choose to show these as well in the graphs. I choose for bar charts in both cases to get a uniform dashboard. The charts were kept plain and simple with labels on top of the bar charts to give a clear overview. I have not removed the y-axis since I still want to see them there from a scientific point of view.

After the feedback I altered some of the initial design choices:

* adapted the chart type for performance in function of height.
* In order to distinguish my main message I therefore adapted the visualisation to show different colors that emphasize the main conclusions.
* adapted the tooltips to get human readable values.

## Feedback

I posted the first version of my visualisations on our company yammer platform in order to receive feedback. I received three comments on the post. 

> Height is a continuous variable so the bar charts are rather contra-intuitive. 

I agreed with the feedback and adapted the chart type for performance in function of height.

> The main message is not very clear yet since 4 charts are provided. It takes some time to understand why this is interesting.

 In order to distinguish my main message I therefore adapted the visualisation to show different colors that emphasize the main conclusions.
 
 > The text in the tooltips is not human readable.
 
 This is something I did not check prior to publishing the first version but I adapted it after the comments.
 
 > The labels from the chart of height in function of batting average are overcrowding the graph
 
The labels have been deleted from the graph since I opted for a different chart type here.
 
  
## Resources

Data was downloaded from:
https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud507/baseball_data.csv&sa=D&ust=1516290329579000&usg=AFQjCNFoi0DgIU4e7LUEgzxMs-sTIjgYWg