import tensorflow as tf

sess=tf.InteractiveSession()

my_tensor=tf.random_uniform([4,4],0,1)#Setting a tensor
my_var=tf.Variable(initial_value=my_tensor)#Defining a Variable
init=tf.global_variables_initializer()#Initializing Variables
sess.run(init)
sess.run(my_var)
