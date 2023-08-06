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

def st_mui_dialog(title: str, content: str, abortlabel: str = "Disagree", agreelabel: str = "Agree", height_open: int = 200,
 fullscreen: bool = False, styling: str = """{"& .MuiModal-backdrop": {"backgroundColor": "rgba(0, 0, 0, 0)"}}""",button_txt : str ="Open Dialog" ,
 button_type: str = "primary", divider : bool = False, key = None) -> int:
    """
    Function to create a Material UI Dialog in streamlit (https://material-ui.com/components/dialogs/) (Alert Dialog)

        :param title: Title of the dialog
        :param content: Content of the dialog

        :param abortlabel: Label of the abort button
        :param agreelabel: Label of the agree button
        :param height_open: Height of the dialog when open (needed to make sure the dialog is not cut off in streamlit)
        :param fullscreen: If the dialog should be fullscreen (whole iframe)
        :param styling: Styling of the dialog (e.g. background color) as json 
        :param divider: If a divider should be shown between the title, the content and the two buttons


        :param button_txt: Text of the button to open the dialog
        :param button_type: Type of the button to open the dialog (primary, secondary, text)


    """

    component_value = _component_func(title = title, content=content,abortlabel= abortlabel, agreelabel = agreelabel, key=key, height=height_open, fullscreen=fullscreen,
     sx = styling, button_txt=button_txt, button_type = button_type, divider = divider, default=None)

    return component_value



#test = "{{'& .MuiModal-backdrop': {'backgroundColor': 'rgba(0, 0, 0, 0)'}}}"