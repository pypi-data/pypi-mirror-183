from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called camera_input_live,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "user_device", path=str(frontend_dir)
)


def user_device(key: Optional[str] = None) -> Optional[str]:
    """
    Add a descriptive docstring
    """
    data: Optional[str] = _component_func(key=key)

    if data is None:
        return None
    return data


def main():
    st.write("## Example")
    device = user_device()
    if device is not None:
        st.write(device)

if __name__ == "__main__":
    main()