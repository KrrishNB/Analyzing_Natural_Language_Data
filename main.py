import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Dataset.xlsx")

##Keeping only the included/filtered sentences that we have found from the data
df_clean= df[df["Include"] == "Yes"].copy()
print("Total Raw SETENCES: ", len(df))
print("After the Filtering took place: " ,  len(df_clean) )
print(f"Academic : {len(df_clean[df_clean['Register'] =="Academic" ])}")
print(f"News: {len(df_clean[df_clean['Register']== 'News'])} ")

## Counting each of the hedges types per each of the Register
cols = ["Epistemic Modal", "Evidential Hedge" , "Approximator"]
counts = df_clean.groupby(['Register',  "Hedge_type"]).size().unstack(fill_value = 0)[cols]

percentages=counts.div(counts.sum(axis = 1 ),axis = 0) *  100
print()
print("Raw Counts: ")
print(counts)
print()
print("Percentages (%) : ")
print(percentages.round(1))

#Making the bar graph to visually represent the distribution
fig ,  ax= plt.subplots(figsize=(9, 6))
x=np.arange(len(cols))
width  =  0.32
colors=['#2C5F8A', '#C0392B']
registers= percentages.index.tolist()

for i, (reg, color) in enumerate(zip(registers ,  colors)):
    vals =  percentages.loc[reg,cols].values
    bars = ax.bar(x + (i - 0.5) * width,vals,width, label = reg,color = color,edgecolor='white' ,  linewidth=0.8)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x()+ bar.get_width()/2,  bar.get_height() +  0.8 ,f'{val:.1f}%' ,  ha = 'center', va = 'bottom',fontsize=9,
                fontweight= 'bold', color = color)
ax.set_xticks(x)
ax.set_xticklabels(cols, fontsize=11)
ax.set_ylabel("Percentage of the SEntence (%) ", fontsize = 12.2)
ax.set_xlabel("Hedge Type" , fontsize=12.2 )
ax.set_title("The Epistemic Hedge Type Distribution: Comparing Academic vs. News (COCA, 2019)", fontsize = 14, fontweight="bold",
            pad =14)
ax.set_ylim(0,62)
ax.yaxis.grid(True, linestyle= "--", alpha=  0.4 )
ax.set_axisbelow(True)
ax.legend(title = "Register",   fontsize= 10, title_fontsize=11, framealpha =0.89, loc ='upper right')
ax.spines["top"].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig("The_Hedge_Type_Dist.png", dpi = 150, bbox_inches= "tight")
plt.show()
print("Fig 1 Saved")