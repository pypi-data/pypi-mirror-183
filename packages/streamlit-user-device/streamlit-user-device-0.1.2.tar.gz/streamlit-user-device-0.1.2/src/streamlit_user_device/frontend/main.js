// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
    Streamlit.setComponentValue(value)
  }
  
  /**
   * The component's render function. This will be called immediately after
   * the component is initially loaded, and then again every time the
   * component gets new data from Python.
   */
  function onRender(event) {
    // Only run the render code the first time the component is loaded.
    if (!window.rendered) {
      var device = "desktop";
      const ua = navigator.userAgent;
      if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {device = "tablet";}
      if (/Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)) {
        device = "mobile";
      }      
      sendValue(device);
      window.rendered = true
    }
  }
  
  // Render the component whenever python send a "render event"
  Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
  // Tell Streamlit that the component is ready to receive events
  Streamlit.setComponentReady()
  // Don't actually need to display anything, so set the height to 0
  Streamlit.setFrameHeight(0)
  