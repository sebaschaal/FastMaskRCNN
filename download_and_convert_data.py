#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from libs.datasets import download_and_convert_coco

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
    'dataset_name2', 'coco',
    'The name of the dataset to convert, one of "cifar10", "flowers", "mnist".')

tf.app.flags.DEFINE_string(
    'dataset_dir2', 'data/coco',
    'The directory where the output TFRecords and temporary files are saved.')


def main(_):
  if not FLAGS.dataset_name2:
    raise ValueError('You must supply the dataset name with --dataset_name')
  if not FLAGS.dataset_dir2:
    raise ValueError('You must supply the dataset directory with --dataset_dir')

  elif FLAGS.dataset_name == 'coco':
    download_and_convert_coco.run(FLAGS.dataset_dir2)
  else:
    raise ValueError(
        'dataset_name [%s] was not recognized.' % FLAGS.dataset_dir2)

if __name__ == '__main__':
  tf.app.run()

