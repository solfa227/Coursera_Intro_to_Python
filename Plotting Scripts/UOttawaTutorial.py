# import csv files to Python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

babynames = pd.read_csv(r'C:\Users\fatem\Downloads\python-workshop-2020-may-master\data\ontariobabynames.csv')
mpg = pd.read_csv(r'C:\Users\fatem\Downloads\python-workshop-2020-may-master\data\mpg.csv')
mpg.head(5)
mpg.columns
mpg.dtypes
mpg.iloc[[1,4,8]]
babynames[babynames["name"].map(len) == 1]["name"].unique()
sns.set()

from matplotlib import rcParams
rcParams['figure.dpi'] = 144

sns.regplot("displ", "hwy", data=mpg, fit_reg=False, color="black" )
sns.scatterplot("displ", "hwy", data=mpg, color="black" )

sns.scatterplot("displ", "hwy", hue="class", data=mpg)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

sns.relplot("displ", "hwy", col="class", data=mpg, col_wrap=3)
sns.relplot("displ", "hwy", col="class", style="drv", data=mpg, col_wrap=3)

p = sns.scatterplot("displ", "hwy", hue="class", data=mpg)
p.set_title("Fuel Efficiency by Engine Size\nData facetted by class")
p.set_xlabel("Engine Size (displacement in liters)")
p.set_ylabel("Fuel Efficiency (MPG)")
p.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.).texts[0].set_text("Vehicle Class")

p = sns.relplot("displ", "hwy", hue="class", data=mpg)
p.axes[0][0].set_title("Fuel Efficiency by Engine Size\nData facetted by class")
p.set_xlabels("Engine Size (displacement in liters)")
p.set_ylabels("Fuel Efficiency (MPG)")
p._legend.texts[0].set_text('Vehicle Class')

p = sns.boxplot(
    x="class",
    y="hwy",
    data=mpg,
    order=["2seater","compact","midsize","minivan","pickup","subcompact","suv"],
    dodge=10
)
p.set_title("Fuel efficiency per class")
p.set_xlabel("Class of vehicle")
p.set_ylabel("Fuel efficiency (in MPG)")
p.set_xticklabels(p.get_xticklabels(), size = 8)
p.set_yticklabels(p.get_yticks(), size = 8)
pass

p=sns.distplot(mpg["hwy"], kde=False, bins=15)
# p.get_figure().savefig("C:\Users\fatem\Downloads\python-workshop-2020-may-master\images\h1.png")

sns.scatterplot("displ", "hwy", hue="class", data=mpg)
sns.lineplot("displ", "hwy", data=mpg)

with sns.diverging_palette(240, 10, n=7):
    sns.scatterplot("displ", "hwy", hue="class", data=mpg)
    
#-------------------------------------------------------

babynames["count"]
babynames[["count"]]
Samira = babynames[babynames["name"] == "Samira"]
babynames[((babynames["count"] == 5) | (babynames["count"] == 6)) & (babynames["year"] == 1920)]
babynames[babynames["name"].isin(["John", "Jon", "Johnny", "Johnnie"])]

babynames.sort_values("count", ascending=False).head(10)
babynames[babynames["count"] > 0].sort_values("count").head(10)

boys_2015 = babynames[(babynames["year"] == 2015) & (babynames["sex"] =="M")]
boys_2015 = boys_2015[["name","count"]]
boys_2015 = boys_2015.sort_values(by="count", ascending=False)
boys_2015 = boys_2015.head(10)
boys_2015

girls_2007 = babynames[(babynames["year"] == 2007) & (babynames["sex"] =="F")]
girls_2007 = girls_2007[["name","count"]]
girls_2007 = girls_2007.sort_values(by="count", ascending=False)
girls_2007 = girls_2007.head(10)
girls_2007

sns.lineplot("year", "count", data=Samira)
sns.lineplot("year", "prop", data=babynames[(babynames["name"] == "Samira") & (babynames["sex"] == "F")])

#----------------------------------------
name_count = babynames[babynames["name"]=="Samira"]
name_count = name_count["count"]
name_count = name_count.sum()
name_count

name_count = babynames[(babynames["name"]=="Samira") & (babynames["count"] > 0)]
name_count = name_count["year"]
name_count = name_count.min()
name_count

#----------------------------------------
babynames_sex_count = babynames.groupby("sex")
babynames_sex_count = babynames_sex_count[["count"]]
babynames_sex_count.sum()

babynames_popularity = babynames.groupby(["name", "sex"])
babynames_popularity = babynames_popularity[["count"]]
babynames_popularity = babynames_popularity.sum()
babynames_popularity = babynames_popularity.sort_values(by="count", ascending=False)
babynames_popularity = babynames_popularity.head(10)
babynames_popularity

#----------------------------------------------
word = "lead"
for letter in word:
    print(letter)

