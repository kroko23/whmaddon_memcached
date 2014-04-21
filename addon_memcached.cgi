#!/usr/bin/perl
#WHMADDON:memcached:Memcached Admin
BEGIN {
    push(@INC,"/usr/local/cpanel");
    push(@INC,"/usr/local/cpanel/whostmgr/docroot/cgi");
      }
      
use CGI ':standard';
use lib '/usr/local/cpanel/';
use Whostmgr::ACLS ();
Whostmgr::ACLS::init_acls();
if (!Whostmgr::ACLS::checkacl( 'restart' ) ) {
        print 'Access Denied.';
        exit;
}
print "Content-type: text/html\n\n";

$header = "<div align=\"center\"><table align=\"center\" width=\"40%\"><tr><td><fieldset>\n";
$footer = "</fieldset></div><center>(c) <a href=\"http://blog.kroko.ro\">Serafin Rusu</a></center>\n";

my $action = param('action');

if ($action eq "") {
        main();
}
if ($action eq "restart") {
        restartmemcached();
}
if ($action eq "start") {
        startmemcached();
}

if ($action eq "stop") {
        stopmemcached();
}


sub main {
        print $header;
        print "<legend>Main Menu</legend>";
        system ("/etc/init.d/memcached status");
        
        print "<br><br><a href=\"?action=restart\">restart</a><br><br><br>\n";
        print "<a href=\"?action=stop\">stop</a><br><br><br>\n";
        print "<a href=\"?action=start\">start</a>\n";
        print $action;
        print $footer;
}


sub restartmemcached {
        print $header;
        print "<legend>Restarted</legend>";
        system ("/etc/init.d/memcached stop");
        print "<br>";
        system ("su - root -c \"/etc/init.d/memcached start\"");
        print $footer;
}

sub startmemcached {
        print $header;
        print "<legend>Start</legend>";
        system("su - root -c \"/etc/init.d/memcached start\"");
        print "<br>";
        system ("/etc/init.d/memcached status");
        print $footer;
}

sub stopmemcached {
        print $header;
        print "<legend>Start</legend>";
        system("su - root -c \"/etc/init.d/memcached stop\"");
        print "<br>";
        system ("/etc/init.d/memcached status");
        print $footer;
}
