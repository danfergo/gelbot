from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC


@interface()
class GHeadInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-head',
    components=[

    ],
    defaults={
        'mjc_interface': GHeadInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                <body>
                    <geom type='capsule' size='0.06 0.1' pos='0 0 -0.15'  mass='1'/>
                </body>

                <geom type='capsule' size='0.05 0.1' pos='0 0 -0.45' mass='1'/> 

                <body name='ankle' pos='0 0 0'/>
            </worldbody>
        </mujoco>
    """
)
class GLeg:
    pass