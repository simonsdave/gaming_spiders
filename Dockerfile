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

FROM simonsdave/cloudfeaster

MAINTAINER Dave Simons

RUN apt-get update -y
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN pip install pip==1.5.6

ADD gaming_spiders gaming_spiders
ADD setup.py .
ADD MANIFEST.in .

RUN python setup.py sdist --formats=gztar

RUN pip install --process-dependency-links dist/gaming_spiders-*.*.*.tar.gz
