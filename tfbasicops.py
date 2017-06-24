import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = x1 * x2
print(result) # this will print a tensor object

result = tf.multiply(x1, x2)

sess = tf.Session()
print(sess.run(result)) # this one also prints a tensor object
sess.close()

with tf.Session() as sess:
	output = sess.run(result)
	print(output)

print(output)