# Installation using pip

This is a guide to installing WeeWX using [pip](https://pip.pypa.io).

## Requirements

- You must have Python 3.7 or later. WeeWX V5 cannot be installed by earlier versions of Python. If you are
constrained by this, install WeeWX V4.9, the last version to support Python 2.7, Python 3.5, and Python 3.6.

- You must also have a copy of pip. Nowadays, almost all versions of Python come with pip, however, if yours does
not, see the pip <a href="https://pip.pypa.io/en/stable/installation/">Installation guide</a>.

- You must have root privileges.


## Installation steps

Installation is a two-step process:

1. Install the software and resources using pip.
2. Create a new station configuration file using the tool `weectl`.

### Install the software and resources using pip

The method discussed below is the simplest way to install WeeWX using pip, but it has some
disadvantages. In particular, it requires root privileges. See the wiki document [pip install
strategies](https://github.com/weewx/weewx/wiki/pip-install-strategies) for some other methods
that avoid this limitation.

```shell
sudo python -m pip install weewx
```

This will download and install any packages required by WeeWX, then install WeeWX itself.

### Create a new configuration file `weewx.conf`

While the first step downloads everything into the Python source tree, it does not set up user data with a
configuration file and skins. That is the goal of the next step, which does not require root privileges

```shell
weectl station create
```

This will create a directory <span class="code">weewx-data</span> in your home directory with a new configuration
file. It will also install skins, documentation, and examples. The same directory will be used to hold the database
file and any generated HTML pages.


## Run

After this, the main program <span class="code">weewxd</span> can be run directly like any other program:

```shell
weewxd
```

### Run as a daemon

<p>
    Follow the following steps to run as a daemon:
</p>

<div class='tabs' id="startup-tabs">
    <nav>
        <button class="tab" onclick="openTab(event, '#startup-debian')">
            Debian <img alt="Debian logo" class='thumbnail' src='images/logo-debian.png'/> <img alt="Ubuntu logo"
                                                                                                class='thumbnail'
                                                                                                src='images/logo-ubuntu.png'/>
            <img alt="Mint logo" class='thumbnail' src='images/logo-mint.png'/>
        </button>
        <button class="tab" onclick="openTab(event, '#startup-redhat')">
            Redhat <img alt="Redhat logo" class='thumbnail' src='images/logo-redhat.png'/> <img alt="Centos logo"
                                                                                                class='thumbnail'
                                                                                                src='images/logo-centos.png'/>
            <img alt="Fedora logo" class='thumbnail' src='images/logo-fedora.png'/>
        </button>
        <button class="tab" onclick="openTab(event, '#startup-suse')">
            SuSE <img alt="SUSE logo" class="thumbnail" src='images/logo-suse.png'/>
        </button>
        <button class="tab" onclick="openTab(event, '#startup-mac')">
            MacOS <img alt="Apple logo" class="thumbnail" src='images/logo-apple.png'/>
        </button>
    </nav>
    <div class="tab-content" id='startup-debian'>
        <pre class="tty cmd"> #-- preferred option - use systemd
sudo weectl daemon install --type=systemd
sudo systemctl enable weewx
sudo systemctl start weewx

#-- option 2 - use the old init.d method if your os is ancient
sudo weectl daemon install --type=sysv
sudo /etc/init.d/weewx start
</pre>
    </div>
    <div class="tab-content" id='startup-redhat'>
        <pre class="tty cmd">sudo weectl daemon install --type=sysv
sudo chkconfig weewx on
sudo /etc/rc.d/init.d/weewx start</pre>
    </div>
    <div class="tab-content" id='startup-suse'>
        <pre class="tty cmd">sudo weectl daemon install --type=sysv
sudo /etc/init.d/weewx start</pre>
    </div>
    <div class="tab-content" id="startup-mac">
        <pre class="tty cmd">sudo weectl daemon install --type=mac
sudo launchctl load /Library/LaunchDaemons/com.weewx.weewxd.plist</pre>
    </div>
</div>


<h2>Logging</h2>
<p>
    On the Mac, WeeWX logs to <span class="code">/var/log/weewx.log</span> by default. Note that this is a privileged
    location: you will need root privileges to run the WeeWX applications.
</p>
<p>
    An alternative is to log to an unprivileged location, allowing you to run applications as any user. For example, to
    log to <span class="code">/var/tmp/weewx.log</span> (an unprivileged location) add this to the end of <span
    class="code">weewx.conf</span>:
</p>
<pre class="tty">
[Logging]
    [[handlers]]
        [[[rotate]]]
            filename = <span class="highlight">/var/tmp/weewx.log</span>
</pre>

<h2>Verify</h2>
<p>After about 5 minutes, open the station web page in a web browser. You should see your station information and data.
    If your hardware supports hardware archiving, then how long you wait will depend on the <a
        href="usersguide.htm#archive_interval">archive interval</a> set in your hardware.
</p>
<pre class='tty'><a href="file:///Users/Shared/weewx/public_html/index.html">file:///Users/Shared/weewx/public_html/index.html</a></pre>

<h2>Customize</h2>
<p>To enable uploads such as Weather Underground or to customize reports, modify the configuration file <span
    class='code'>/Users/Shared/weewx/weewx.conf</span>. See the <a href="usersguide.htm">User Guide</a> and <a
    href="customizing.htm">Customization Guide</a> for details.
</p>

<p>WeeWX must be restarted for configuration file changes to take effect.
</p>

<h2>Start/Stop</h2>
<p>To start/stop WeeWX:</p>
<pre class='tty cmd'>sudo launchctl load /Library/LaunchDaemons/com.weewx.weewxd.plist
sudo launchctl unload /Library/LaunchDaemons/com.weewx.weewxd.plist</pre>

<h2>Uninstall</h2>

<p>
    First, stop WeeWX.
</p>

<p>
    Second, uninstall any daemon services.
</p>

<pre class="tty cmd">sudo weectl daemon uninstall</pre>

<p>
    Third, use pip to uninstall the weewx software and its dependencies. Make sure some other software is not using the
    dependencies before uninstalling them!
</p>

<pre class='tty cmd'>pip uninstall weewx configobj CT3 pyephem ephem Pillow pyusb pyserial pymysql -y</pre>

<p>
    Finally, if desired, uninstall the data directory:
</p>

<pre class="tty cmd">rm -r ~/weewx-data</pre>


<h2>Layout</h2>
<p>The instructions above will result in the following layout:</p>
<table class='locations' style="width: auto;">
    <tr>
        <td align='right'>executable:</td>
        <td class='tty'>/Users/Shared/weewx/bin/weewxd</td>
    </tr>
    <tr>
        <td align='right'>configuration file:</td>
        <td class='tty'>/Users/Shared/weewx/weewx.conf</td>
    </tr>
    <tr>
        <td align='right'>skins and templates:</td>
        <td class='tty'>/Users/Shared/weewx/skins/</td>
    </tr>
    <tr>
        <td align='right'>sqlite databases:</td>
        <td class='tty'>/Users/Shared/weewx/archive/</td>
    </tr>
    <tr>
        <td align='right'>generated web pages and images:</td>
        <td class='tty'>/Users/Shared/weewx/public_html/</td>
    </tr>
    <tr>
        <td align='right'>documentation:</td>
        <td class='tty'>/Users/Shared/weewx/docs/</td>
    </tr>
    <tr>
        <td align='right'>examples:</td>
        <td class='tty'>/Users/Shared/weewx/examples/</td>
    </tr>
    <tr>
        <td align='right'>utilities:</td>
        <td class='tty'>/Users/Shared/weewx/bin/wee_*</td>
    </tr>
</table>

<p class='copyright'>
    &copy; <a href='copyright.htm'>Copyright</a> Tom Keffer
</p>

</body>
</html>
