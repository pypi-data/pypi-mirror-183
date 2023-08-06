import streamlit.components.v1 as components
import os

_RELEASE = False


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_mui_dialog",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_mui_dialog", path=build_dir)

def st_mui_dialog(title: str, content: str, abortlabel: str = "Disagree", agreelabel: str = "Agree", height_open: int = 300,
 fullscreen: bool = False, styling_dialog: str = """{"& .MuiModal-backdrop": {"backgroundColor": "rgba(0, 0, 0, 0)"}}""", button_txt : str ="Open Dialog" ,
 button_open_type: str = "primary", button_abort_type: str = "primary",button_agree_type: str = "primary", divider : bool = False, styling_open_button : str = """{"placeholder":{"bgcolor":"none"}}""", styling_agree_button : str = """{"placeholder":{"bgcolor":"none"}}""",
  styling_abort_button : str = """{"placeholder":{"bgcolor":"none"}}""", width_dialog: str = "sm", adapt_width_dialog: bool = False,
  styling_dialog_content : str = """{"placeholder":{"bgcolor":"none"}}""", styling_dialog_title : str = """{"placeholder":{"bgcolor":"none"}}""",
  styling_dialog_content_text : str = """{"placeholder":{"bgcolor":"none"}}""",
  transition_mode: str = "fade", slide_direction: str = "up", on_agree: str = "", on_abort:str = "", on_close:str = "", on_open:str = "", key = None) -> int:
    """
    Function to create a Material UI Dialog in streamlit (https://material-ui.com/components/dialogs/) (Alert Dialog)

        :param title: Title of the dialog
        :param content: Content of the dialog

        :param abortlabel: Label of the abort button
        :param agreelabel: Label of the agree button
        :param height_open: Height of the dialog when open (needed to make sure the dialog is not cut off in streamlit)
        :param fullscreen: If the dialog should be fullscreen (whole iframe)
        :param divider: If a divider should be shown between the title, the content and the two buttons

        :param styling_dialog: Styling of the dialog (e.g. background color) as json 
        :param styling_open_button: Styling of the button to open the dialog (e.g. background color) as json
        :param styling_agree_button: Styling of the agree button (e.g. background color) as json
        :param styling_abort_button: Styling of the abort button (e.g. background color) as json
        :param styling_dialog_content: Styling of the content of the dialog (e.g. background color) as json
        :param styling_dialog_title: Styling of the title of the dialog (e.g. background color) as json
        :param styling_dialog_content_text: Styling of the text of the content of the dialog (e.g. background color) as json

        :param transition_mode: Transition mode of the dialog (fade, slide, zoom, grow)
        :param slide_direction: Slide direction of the dialog (up, down, left, right) (only needed if Transition mode is slide)

        :param width_dialog: Width of the dialog (None,xs, sm, md, lg, xl)
        :param adapt_width_dialog: Streches the dialog to the full maximum width

        :param button_txt: Text of the button to open the dialog
        :param button_open_type: Type of the button to open the dialog (primary, secondary, ...)

        :param button_abort_type: Type of the abort button (primary, secondary, ...)
        :param button_agree_type: Type of the agree button (primary, secondary, ...)

        :param key: Key of the component (needed if multiple components are used on the same page)


    """

    component_value = _component_func(title = title, content=content,abortlabel= abortlabel, agreelabel = agreelabel, key=key, height=height_open, fullscreen=fullscreen,
     styling_dialog = styling_dialog, button_txt=button_txt, button_type = button_open_type, divider = divider, styling_open_button = styling_open_button, styling_agree_button = styling_agree_button,
     styling_abort_button = styling_abort_button, width_dialog = width_dialog, adapt_width_dialog = adapt_width_dialog, styling_dialog_content = styling_dialog_content,
     styling_dialog_title = styling_dialog_title, styling_dialog_content_text = styling_dialog_content_text, transition_mode = transition_mode, 
     slide_direction = slide_direction, button_abort_type = button_abort_type, button_agree_type = button_agree_type, on_agree = on_agree,
     on_abort = on_abort, on_close = on_close, on_open = on_open, default=None)

    return component_value

