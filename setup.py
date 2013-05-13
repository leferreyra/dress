from distutils.core import setup
import py2exe

opt = {
    "py2exe":{
        "packages":["wx.lib.pubsub"]
    }
}

setup(
    windows=[
            {
                "script":"app.py",
            }
        ],
    options=opt
)
