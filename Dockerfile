# to build the image
#
#   sudo docker build -t simonsdave/gaming_spiders .
#
# for testing/debugging
#
#   sudo docker run -i -t simonsdave/gaming_spiders /bin/bash
#
# to push to dockerhub
#
#   sudo docker push simonsdave/gaming_spiders
#

FROM simonsdave/spidering:14.04

MAINTAINER Dave Simons

ADD dist/gaming_spiders-1.0.0.tar.gz /tmp/.
RUN pip install --process-dependency-links /tmp/gaming_spiders-1.0.0
