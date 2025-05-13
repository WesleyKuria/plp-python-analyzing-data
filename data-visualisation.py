plt.figure(figsize=(10,5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', color='blue')
plt.title("Sepal Length Trend Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

# bar chart
grouped['petal length (cm)'].plot(kind='bar', color='orange')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.grid(axis='y')
plt.show()

# histogram
plt.hist(df['sepal width (cm)'], bins=15, color='green', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

#scatter plot
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
