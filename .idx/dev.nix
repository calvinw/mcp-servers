# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  # channel = "stable-24.05"; # or "unstable"
  channel = "unstable"; 
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python313
    pkgs.python313Packages.pip
    pkgs.nodejs_20
    pkgs.uv
    pkgs.dolt
    pkgs.pspg
    
    # Core browser dependencies - comprehensive set based on research
    pkgs.chromium
    pkgs.glib
    pkgs.nspr
    pkgs.nss
    pkgs.atk
    pkgs.at-spi2-atk
    pkgs.gtk3
    pkgs.gdk-pixbuf
    pkgs.cairo
    pkgs.pango
    pkgs.dbus
    pkgs.systemd
    pkgs.libgbm
    pkgs.mesa
    pkgs.mesa.drivers
    pkgs.libdrm
    
    # X11 and display libraries
    pkgs.xorg.libX11
    pkgs.xorg.libxcb
    pkgs.xorg.libXi
    pkgs.xorg.libXext
    pkgs.xorg.libXfixes
    pkgs.xorg.libXrandr
    pkgs.xorg.libXrender
    pkgs.xorg.libXdamage
    pkgs.xorg.libXcomposite
    pkgs.xorg.libXcursor
    pkgs.xorg.libXinerama
    pkgs.xorg.libXScrnSaver
    pkgs.xorg.libXtst
    pkgs.xorg.libxshmfence
    
    # Audio and other system libraries
    pkgs.alsa-lib
    pkgs.cups
    pkgs.expat
    pkgs.fontconfig
    pkgs.freetype
    pkgs.libxkbcommon
    pkgs.libGL
    pkgs.shared-mime-info
    
    # Additional libraries commonly needed by Chromium
    pkgs.libuuid
    pkgs.libsecret
    pkgs.libappindicator-gtk3
    pkgs.liberation_ttf
  ];
  
  # Enable nix-ld for running unpatched binaries
  env = {
    # Core nix-ld setup
    NIX_LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath [
      # Core system libraries
      pkgs.glib
      pkgs.nspr
      pkgs.nss
      pkgs.atk
      pkgs.at-spi2-atk
      pkgs.gtk3
      pkgs.gdk-pixbuf
      pkgs.cairo
      pkgs.pango
      pkgs.dbus
      pkgs.systemd
      pkgs.libgbm
      pkgs.mesa
      pkgs.mesa.drivers
      pkgs.libdrm
      
      # X11 libraries
      pkgs.xorg.libX11
      pkgs.xorg.libxcb
      pkgs.xorg.libXi
      pkgs.xorg.libXext
      pkgs.xorg.libXfixes
      pkgs.xorg.libXrandr
      pkgs.xorg.libXrender
      pkgs.xorg.libXdamage
      pkgs.xorg.libXcomposite
      pkgs.xorg.libXcursor
      pkgs.xorg.libXinerama
      pkgs.xorg.libXScrnSaver
      pkgs.xorg.libXtst
      pkgs.xorg.libxshmfence
      
      # Audio and other libraries
      pkgs.alsa-lib
      pkgs.cups
      pkgs.expat
      pkgs.fontconfig
      pkgs.freetype
      pkgs.libxkbcommon
      pkgs.libGL
      pkgs.shared-mime-info
      pkgs.libuuid
      pkgs.libsecret
      pkgs.libappindicator-gtk3
    ]}";
    NIX_LD = "${pkgs.glibc}/lib/ld-linux-x86-64.so.2";
    
    # Puppeteer configuration for Nix environment
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD = "false";
    PUPPETEER_EXECUTABLE_PATH = "${pkgs.chromium}/bin/chromium";
    
    # Additional Chrome/Chromium flags for web IDE compatibility
    CHROME_DEVEL_SANDBOX = "${pkgs.chromium}/bin/chromium";
    CHROMIUM_FLAGS = "--no-sandbox --disable-setuid-sandbox --disable-dev-shm-usage --disable-gpu --remote-debugging-port=9222";
    
    # Font configuration
    FONTCONFIG_FILE = "${pkgs.fontconfig.out}/etc/fonts/fonts.conf";
    
    # Additional environment variables that may help
    DISPLAY = ":99";
    XDG_RUNTIME_DIR = "/tmp";
  };
  
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
    ];
    # Enable previews
    previews = {
      enable = true;
      previews = {
         web = {
           # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
           # and show it in IDX's web preview panel
           command = ["sh" "-c" "mcp-greet/run_chainlit.sh"];
           manager = "web";
           env = {
             # Environment variables to set for your server
             PORT = "$PORT";
           };
         };
      };
    };
    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Example: install JS dependencies from NPM
        # npm-install = "npm install";
        # Open editors for the following files by default, if they exist:
        # default.openFiles = [ ];
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
      };
    };
  };
}
