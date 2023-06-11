from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC


@interface()
class GFootInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-foot',
    components=[

    ],
    defaults={
        'mjc_interface': GFootInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                <geom type='box' size='0.06 0.1 0.03' pos='0 0.05 0.03' mass='1'/>
            </worldbody>
        </mujoco>
    """
)
class GFoot:
    pass