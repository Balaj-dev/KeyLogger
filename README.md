# KeyLogger
An educational cybersecurity project , A key logger which records all the keys written or clicked by a user and works in background.
<h1>Disclaimer</h1>
<b><p>This project is created strictly for educational and research purposes.
Its purpose is to demonstrate my programming skills, security understanding, and practical learning in the field of cybersecurity. </p></b>
<ul>
  <li>
    Do NOT use this software for any unauthorized activity.
  </li>
  <li>
    Do NOT deploy it on any device, system, or network without explicit written permission from the owner.
  </li>
  <li>
    Unauthorized keylogging is illegal, violates privacy laws, and can result in serious criminal penalties.
  </li>
  <li>
    The author is not responsible for any misuse, damage, or legal consequences caused by third-party use of this code.
  </li>
</ul>
<p>By using or downloading this project, you agree that it is your responsibility to comply with all applicable laws and obtain proper authorization.</p>

<hr>

<h2>📂 Project File Structure</h2>

<pre><code>
Keylogger/
│
├── main.py                 # Main keylogger script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore
│
└── logs/                   # Folder where key logs are stored
    ├── log_files_id_info.txt           # Info about each keylogger session
    └── 2025-11-22_18-40_Keylogger_data.txt  # Key log file
</code></pre>

<hr>

<h2>⚙ How It Works</h2>

<ul>
  <li>Uses the <code>pynput</code> library to listen for all keyboard inputs.</li>
  <li>Each key press is logged into a file inside the <code>logs/</code> folder.</li>
  <li>Special keys like <code>Enter</code>, <code>Space</code>, and <code>Backspace</code> are handled properly.</li>
  <li>A separate info file (<code>log_files_id_info.txt</code>) records the start and end time of each session.</li>
  <li>Filenames are timestamped to ensure uniqueness and cross-platform safety.</li>
</ul>

<hr>

<h2>💻 Installation & Usage</h2>

<p>These steps work on Windows, macOS, and Linux:</p>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/Balaj-dev/KeyLogger.git
cd your-repo</code></pre>

<h3>2. Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3. Run the keylogger</h3>
<pre><code>python main.py</code></pre>

<p>If your system uses <code>python3</code>, use:</p>
<pre><code>python3 main.py</code></pre>

<p><strong>macOS users:</strong> Go to <em>System Settings → Privacy & Security → Input Monitoring</em> and allow Python/Terminal to capture keyboard input.</p>

<hr>

<h2>📁 Output</h2>

<p>All logs are saved inside the <code>logs/</code> folder:</p>

<pre><code>
logs/
│── log_files_id_info.txt                # Info about start/end of sessions
└── 2025-11-22_18-40_Keylogger_data.txt # Key presses for this session
</code></pre>

<hr>

<h2>⚠ Legal Notice</h2>
<p class="note">This project is intended for <strong>educational purposes only</strong>. Do <strong>not</strong> use it to capture keystrokes from others without explicit permission, as it may be illegal in your jurisdiction.</p>
