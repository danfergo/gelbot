from yarok import ConfigBlock, component, interface
from yarok.platforms.mjc import InterfaceMJC

from worlds.components.g02_hand import GHand
from worlds.components.g03_arm import GArm
from worlds.components.g04_torso import GTorso
from worlds.components.g05_leg import GLeg
from worlds.components.g06_foot import GFoot


@interface()
class GBotInterfaceMJC:
    def __init__(self, interface: InterfaceMJC):
        self.interface = interface


@component(
    tag='g-bot',
    defaults={
        'mjc_interface': GBotInterfaceMJC
    },
    components=[
        GArm,
        GHand,
        GTorso,
        GLeg,
        GFoot
    ],
    # language=xml
    template="""
        <mujoco>
            <worldbody>
                <joint type="free"/>
                <body pos="0 0 0.5">
                     <g-torso name="g-torso" pos="0 0 0.1"> 
                        <g-arm name="left-arm" parent="left-arm">
                            <g-hand name="left-hand" parent="wrist"/>
                        </g-arm>
                       
                        <g-arm name="right-arm" parent="right-arm">
                            <g-hand name="right-hand" parent="wrist"/>
                        </g-arm>
                        
                        <g-leg name="left-leg" parent="left-hip">
                            <g-foot name="left-foot" parent="ankle"/> 
                        </g-leg>
                        
                        <g-leg name="right-leg" parent="right-hip">
                            <g-foot name="right-foot" parent="ankle"/>
                        </g-leg>  
                    </g-torso>
                </body> 
            </worldbody>
        </mujoco>
    """
)
class GBot:
    pass
