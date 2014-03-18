#! /usr/bin/python

# This is a script for blog savvies
# it enable you deploy one post(in markdown format) to many sites
# currently support:
#   - jekyll
#   - octopress
#   - hexo
#   - wordpress
#   - tumblr 

import subprocess
import os
import argparse
import markdown2
import datetime, xmlrpclib
import pytumblr

################################
## global variables ############
################################
OCTOPRESS="";     ### PLEASE fill your local octopress setting path here, such as "/Users/username/octopress"
POSTOCTOPRESS=OCTOPRESS + "/source/_posts";
JEKYLL=""         ### PLEASE fill your local jekyll setting path here, such as "/Users/username/jekyll";
POSTJEKYLL=JEKYLL + "/_posts";
HEXO=""           ### PLEASE fill your local hexo setting path here, such as "/Users/username/hexo";
POSTHEXO=HEXO + "/source/_posts";
##configuration for wordpress
wp_url = "http://domainname/xmlrpc.php"    ### PLEASE fill xmlrpc.php address correct
wp_username = "username"
wp_password = "password"
wp_blogid = ""
status_draft = 0
status_published = 1

##configuration for tumblr 
# Authenticate via OAuth
TUMBLR=""                                 ### PLEASE fill TUMBLR="YES" if you intend to set up tumblr blog
client = pytumblr.TumblrRestClient(
        'consumer key',
        'consumer secret',
        'oauth token',
        'oauth secret'
              )

### parse arguments
parser = argparse.ArgumentParser(description='markdown file to deploy');
parser.add_argument('mdfile', nargs='+', help='markdown file to deploy');
args = parser.parse_args();
inputname= args.mdfile[0];
inputtitle=inputname[:-3];
newoctopress= 'new_post[%s]' %(inputtitle);
newjekyll= 'title=%s' %(inputtitle);
print newoctopress;
print newjekyll;
fin=open(inputname,"r");
fdata=fin.read();
fin.close();


print '=======wordpress=====\n'
################################
## wordpress section ###########
################################
if (wp_url):
    wordpresspost= markdown2.markdown(fdata)   ##wordpress post in html format
    wordpresspost = " %s" %(wordpresspost)
    server = xmlrpclib.ServerProxy(wp_url)
    title = inputtitle 
    date_created = xmlrpclib.DateTime(datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M"))
    ## fill the category and tag if you need
    categories = []
    tags = []
    data = {'title': title, 'description': wordpresspost, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}
    post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)

print '=======tumblr========\n'
################################
## tumblr section ##############
################################
if (TUMBLR):
    client.create_text('username.tumblr.com',format='markdown',title=inputtitle,body=fdata)

print '=======octopress========\n'
################################
## octopress section ###########
################################
if (OCTOPRESS):
    subprocess.check_call(('bundle', 'exec', 'rake',newoctopress), cwd=OCTOPRESS); 
    ## look for latest file in source/_posts/ directory and append markdown file in the input arguments to it
    files = [os.path.join(POSTOCTOPRESS, fname) for fname in os.listdir(POSTOCTOPRESS)];
    lastoctopress = max(files, key=os.path.getmtime);
    print lastoctopress;
    fout = open(lastoctopress,"a");
    fout.write(fdata);
    fout.close();
    
    ## generate site
    subprocess.check_call(('bundle', 'exec', 'rake','generate'), cwd=OCTOPRESS); 
    ## deploy site
    subprocess.check_call(('bundle', 'exec', 'rake','deploy'), cwd=OCTOPRESS);

print '=======jekyll========\n'
################################
## jekyll section  #############
################################
if (JEKYLL):
    subprocess.check_call(('bundle','exec','rake','post',newjekyll), cwd=JEKYLL);
    ## look for latest file in source/_posts/ directory and append markdown file in the input arguments to it
    files = [os.path.join(POSTJEKYLL, fname) for fname in os.listdir(POSTJEKYLL)];
    lastjekyll = max(files, key=os.path.getmtime);
    print lastjekyll;
    fout = open(lastjekyll,"a");
    fout.write(fdata);
    fout.close();
    jekyllmessage="commit %s post" %(inputname);
    subprocess.check_call(('git','add','.'), cwd=JEKYLL);
    subprocess.check_call(('git','commit','-m',jekyllmessage), cwd=JEKYLL);
    subprocess.check_call(('git','push','origin','gh-pages'), cwd=JEKYLL);

print '=======hexo==========\n'
################################
## hexo section ################
################################
if (HEXO):
    subprocess.check_call(('hexo','new',inputtitle), cwd=HEXO);
    ## look for latest file in source/_posts/ directory and append markdown file in the input arguments to it
    files = [os.path.join(POSTHEXO, fname) for fname in os.listdir(POSTHEXO)];
    lasthexo = max(files, key=os.path.getmtime);
    print lasthexo;
    fin=open(inputname,"r");
    fdata=fin.read();
    fin.close();
    fout = open(lasthexo,"a");
    fout.write(fdata);
    fout.close();
    subprocess.check_call(('hexo','deploy','--generate'), cwd=HEXO);



