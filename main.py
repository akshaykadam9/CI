import matplotlib.pyplot as plt

def ab(a,b):
    return a+b
 
def cd(c,d):
    return c-d

def ak():
    return 'hello akshay, I am damm sure that you will become a best Data Scientist'


fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [140, 10, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.savefig('bars.png', bbox_inches='tight')

print(ab(4,5))
print(cd(10,5))
print(ak())