from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC


@interface()
class GFingerInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-finger',
    defaults={
        'mjc_interface': GFingerInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                <geom type='capsule' size='0.01 0.02' pos='0 0 0.03' mass='0.1'/>
                
                <body pos='0 0 0.06'>
                    <geom type='capsule' size='0.01 0.02' pos='0 0 0.03' mass='0.1'/>
                </body>
            </worldbody>
        </mujoco>
    """
)
class GFinger:
    pass