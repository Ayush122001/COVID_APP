FROM ayush122001/keras-flask:v1

RUN yum install httpd -y

COPY index.html /var/www/html/index.html 

COPY form.html /var/www/html/form.html

COPY safe.html /var/www/html/safe.html

COPY fail.html /var/www/html/fail.html

COPY nBar.html /var/www/html/nBar.html

COPY home.html /var/www/html/home.html

COPY about.html /var/www/html/about.html

COPY safe.jpg /var/www/html/safe.jpg

COPY my.jpg /var/www/html/my.jpg

COPY home1.jpg /var/www/html/home1.jpg

COPY form.jpg /var/www/html/form.jpg

COPY fail.jpg /var/www/html/fail.jpg

CMD ["/usr/sbin/httpd", "-D","FOREGROUND"]

