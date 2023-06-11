from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC


@interface()
class GLegInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-leg',
    components=[

    ],
    defaults={
        'mjc_interface': GLegInterfaceMJC
    },
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                    <body>
                        <geom type='capsule' size='0.06 0.1' pos='0 0 -0.1' mass='1'/>
                    </body>
                    
                    <geom type='capsule' size='0.05 0.1' pos='0 0 -0.41' mass='1'/> 
    
                    <body name='ankle' pos='0 0 -0.6'/>
            </worldbody>
        </mujoco>
    """
)
class GLeg:
    pass