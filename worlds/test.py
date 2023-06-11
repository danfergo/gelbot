from yarok import Platform, PlatformMJC, PlatformHW, ConfigBlock, Injector, component

from yarok.comm.plugins.cv2_waitkey import Cv2WaitKey

from worlds.components.g00_bot import GBot
from worlds.components.g06_foot import GFoot


@component(
    components=[
        GBot,
        GFoot
    ],
    template="""
        <mujoco>
            <compiler angle="radian"/>

            <visual>
                <!-- important for the Geltips, to ensure the its camera frustum captures the close-up elastomer -->
                <map znear="0.001" zfar="50"/>
                <quality shadowsize="2048"/>
            </visual>

            <asset>
                <!-- empty world -->
                <texture name="texplane" type="2d" builtin="checker" rgb1=".2 .3 .4" rgb2=".1 0.15 0.2"
                         width="512" height="512" mark="cross" markrgb=".8 .8 .8"/>    
                <material name="matplane" reflectance="0.3" texture="texplane" texrepeat="1 1" texuniform="true"/> 
                

                <!-- materials -->
                <material name="black_plastic" rgba=".3 .3 .3 1"/>
                
                <!-- meshes -->
                <!-- <mesh name="object" file="assets/mesh.stl" scale="0.001 0.001 0.001"/>  -->
            </asset>

            <worldbody>
                <light directional="true" diffuse=".9 .9 .9" specular="0.1 0.1 0.1" pos="0 0 5.0" dir="0 0 -1"/>
                <camera name="viewer" pos="0 0 0.5" mode="fixed" zaxis="0 0 1"/>

                <body name="floor">
                    <geom name="ground" type="plane" size="0 0 1" pos="0 0 0" quat="1 0 0 0" material="matplane" condim="1"/>
                </body>
                
                <body pos="0 0 0.1">
                    <g-bot name="robot"/>
                </body>
                
                <!--
                <body pos="1 1 0" >
                    <g-foot name="footx"/>
                </body> -->
            </worldbody>    
        </mujoco>
    """
)
class SomeWorld:
    pass


class SomeBehaviour:

    def __init__(self, injector: Injector, config: ConfigBlock, pl: Platform):
        self.pl = injector.get(Platform)
        self.config = injector.get(ConfigBlock)
        # self.eg_robot = injector.get('eg_robot')

    def on_start(self):
        # self.pl.wait(lambda: ...)
        self.pl.wait_seconds(1)

    def on_update(self):
        return True


def main():
    Platform.create({
        'world': SomeWorld,
        'behaviour': SomeBehaviour,
        'defaults': {
            'environment': 'sim',
            'behaviour': {
                'some_conf': 'some_value'
            },
            'components': {
                '/': {
                    'world_conf': 'world_conf_value'
                }
            },
            'plugins': [
                (Cv2WaitKey, {})
            ]
        }
    }).run()


if __name__ == '__main__':
    main()
