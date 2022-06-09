"""Test main module."""

from dotenv import load_dotenv

# from anomaly_data_viz.app import App


def test_main():
    """Test main() method."""
    env_loaded = load_dotenv()
    # main()
    # app = import_app("dash_test.app.App.app")
    # app.layout = html.Div(id="nully-wrapper", children=0)
    # 4. host the app locally in a thread, all dash server configs could be
    # passed after the first app argument
    # dash_duo.start_server(app)
    # 5. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    # dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)
    # 6. use this form if its present is expected at the action point
    #   assert dash_duo.find_element("#nully-wrapper").text == "0"
    # 7. to make the checkpoint more readable, you can describe the
    # acceptance criterion as an assert message after the comma.
    # assert dash_duo.get_logs() == [], "browser console should contain no error"
    assert env_loaded is True
