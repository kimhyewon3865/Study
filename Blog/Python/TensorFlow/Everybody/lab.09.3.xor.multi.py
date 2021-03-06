import tensorflow as tf
import numpy as np

x_data = np.array([[0,0], [0,1], [1,0], [1,1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

num_input = 2
l1_l2 = 10
W1 = tf.Variable(tf.random_normal([num_input, l1_l2]))
b1 = tf.Variable(tf.random_normal([l1_l2]))
h1 = tf.sigmoid(tf.matmul(X, W1) + b1)

l2_l3 = 4
W2 = tf.Variable(tf.random_normal([l1_l2, l2_l3]))
b2 = tf.Variable(tf.random_normal([l2_l3]))
h2 = tf.sigmoid(tf.matmul(h1, W2) + b2)

W3 = tf.Variable(tf.random_normal([l2_l3, 1]))
b3 = tf.Variable(tf.random_normal([1]))

hypothesis = tf.sigmoid(tf.matmul(h2, W3) + b3)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1- hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

feed_dict = {X: x_data, Y: y_data}
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train, feed_dict=feed_dict)

        if step % 1000 == 0:
            print(step, sess.run(cost, feed_dict=feed_dict))

    print(sess.run([hypothesis, predicted, accuracy], feed_dict=feed_dict))
