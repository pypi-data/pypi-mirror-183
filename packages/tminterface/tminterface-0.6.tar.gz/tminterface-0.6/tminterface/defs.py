from bytefields import *

class PlayerInfoStruct(ByteStruct):
    team                = IntegerField(offset=576, signed=False)
    prev_race_time      = IntegerField(offset=680)
    race_start_time     = IntegerField(offset=prev_race_time, signed=False)
    race_time           = IntegerField(offset=race_start_time, signed=True)
    race_best_time      = IntegerField(offset=race_time, signed=False)
    lap_start_time      = IntegerField(offset=race_best_time, signed=False)
    lap_time            = IntegerField(offset=lap_start_time, signed=False)
    lap_best_time       = IntegerField(offset=lap_time)
    min_respawns        = IntegerField(offset=lap_best_time, signed=False)
    nb_completed        = IntegerField(offset=min_respawns, signed=False)
    max_completed       = IntegerField(offset=nb_completed, signed=False)
    stunts_score        = IntegerField(offset=max_completed, signed=False)
    best_stunts_score   = IntegerField(offset=stunts_score, signed=False)
    cur_checkpoint      = IntegerField(offset=best_stunts_score, signed=False)
    average_rank        = FloatField(offset=cur_checkpoint)
    current_race_rank   = IntegerField(offset=average_rank, signed=False)
    current_round_rank  = IntegerField(offset=current_race_rank, signed=False)
    current_time        = IntegerField(offset=776, signed=False)
    race_state          = IntegerField(offset=788, signed=False)
    ready_enum          = IntegerField(offset=race_state, signed=False)
    round_num           = IntegerField(offset=ready_enum, signed=False)
    offset_current_cp   = FloatField(offset=round_num)
    cur_lap_cp_count    = IntegerField(offset=816, signed=False)
    cur_cp_count        = IntegerField(offset=cur_lap_cp_count, signed=False)
    cur_lap             = IntegerField(offset=cur_cp_count, signed=False)
    race_finished       = BooleanField(offset=cur_lap)
    display_speed       = IntegerField(offset=race_finished)
    finish_not_passed   = BooleanField(offset=display_speed)
    countdown_time      = IntegerField(offset=916)
    rest                = ByteArrayField(countdown_time, 32)


class HmsDynaStateStruct(ByteStruct):
    quat                        = ArrayField(offset=0, shape=(4,), elem_field_type=FloatField)
    rotation                    = ArrayField(quat, shape=(3, 3), elem_field_type=FloatField)
    position                    = ArrayField(rotation, shape=(3,), elem_field_type=FloatField)
    linear_speed                = ArrayField(position, shape=(3,), elem_field_type=FloatField)
    add_linear_speed            = ArrayField(linear_speed, shape=(3,), elem_field_type=FloatField)
    angular_speed               = ArrayField(add_linear_speed, shape=(3,), elem_field_type=FloatField)
    force                       = ArrayField(angular_speed, shape=(3,), elem_field_type=FloatField)
    torque                      = ArrayField(force, shape=(3,), elem_field_type=FloatField)
    inverse_intertia_tensor     = ArrayField(torque, shape=(3, 3), elem_field_type=FloatField)
    unknown                     = FloatField(inverse_intertia_tensor)
    not_tweaked_linear_speed    = ArrayField(unknown, shape=(3,), elem_field_type=FloatField)
    owner                       = IntegerField(not_tweaked_linear_speed)


class HmsDynaStruct(ByteStruct):
    previous_state = StructField(268, struct_type=HmsDynaStateStruct)
    current_state = StructField(previous_state, struct_type=HmsDynaStateStruct)
    prev_state = StructField(current_state, struct_type=HmsDynaStateStruct)
    rest = ByteArrayField(prev_state, 616)


class SurfaceHandler(ByteStruct):
    unknown = ArrayField(offset=4, shape=(4, 3), elem_field_type=FloatField)
    rotation = ArrayField(unknown, shape=(3, 3), elem_field_type=FloatField)
    position = ArrayField(rotation, shape=3, elem_field_type=FloatField)    


class RealTimeState(ByteStruct):
    damper_absorb = FloatField(0)
    field_4 = FloatField(4)
    field_8 = FloatField(8)
    field_12 = ArrayField(12, shape=(3, 3), elem_field_type=FloatField)
    field_48 = ArrayField(field_12, shape=(3, 3), elem_field_type=FloatField)
    field_84 = ArrayField(field_48, shape=3, elem_field_type=FloatField)
    field_108 = FloatField(108)
    has_ground_contact = BooleanField(field_108)
    contact_material_id = IntegerField(has_ground_contact)
    is_sliding = BooleanField(contact_material_id)
    relative_rotz_axis = ArrayField(is_sliding, shape=3, elem_field_type=FloatField)
    nb_ground_contacts = IntegerField(140)
    field_144 = ArrayField(nb_ground_contacts, shape=3, elem_field_type=FloatField)
    rest = ByteArrayField(field_144, 12)


class WheelState(ByteStruct):
    rest = ByteArrayField(0, 100)


class SimulationWheel(ByteStruct):
    steerable = BooleanField(offset=4)
    field_8 = IntegerField(steerable)
    surface_handler = StructField(field_8, SurfaceHandler)
    field_112 = ArrayField(surface_handler, shape=(4, 3), elem_field_type=FloatField)
    field_160 = IntegerField(field_112)
    field_164 = IntegerField(field_160)
    offset_from_vehicle = ArrayField(field_164, shape=3, elem_field_type=FloatField)
    real_time_state = StructField(offset_from_vehicle, RealTimeState)
    field_348 = IntegerField(real_time_state)
    contact_relative_local_distance = ArrayField(field_348, shape=3, elem_field_type=FloatField)
    prev_sync_wheel_state = StructField(contact_relative_local_distance, WheelState)
    sync_wheel_state = StructField(prev_sync_wheel_state, WheelState)
    field_564 = StructField(sync_wheel_state, WheelState)
    async_wheel_state = StructField(field_564, WheelState)


class CheckpointTime(ByteStruct):
    time = IntegerField(offset=0)
    stunts_score = IntegerField(time)


class CheckpointData(ByteStruct):
    reserved = IntegerField(offset=0)
    cp_states_length = IntegerField(reserved)
    cp_states = ArrayField(cp_states_length, shape=None, elem_field_type=BooleanField)
    cp_times_length = IntegerField(cp_states)
    cp_times = ArrayField(cp_times_length, shape=None, elem_field_type=CheckpointTime)


class InputEvent(ByteStruct):
    time = IntegerField(offset=0)
    input_data = IntegerField(time)


class CachedInput(ByteStruct):
    time = IntegerField(offset=0)
    event = StructField(time, InputEvent)


class SceneVehicleCarState(ByteStruct):
    speed_forward = FloatField(offset=0)
    speed_slideward = FloatField(speed_forward)
    input_steer = FloatField(speed_slideward)
    input_gas = FloatField(input_steer)
    input_brake = FloatField(input_gas)
    is_turbo = BooleanField(input_brake)
    rpm = FloatField(offset=128)
    gearbox_state = IntegerField(offset=136)
    rest = ByteArrayField(gearbox_state, 28)


class Engine(ByteStruct):
    max_rpm = FloatField(offset=0)
    braking_factor = FloatField(20)
    clamped_rpm = FloatField(braking_factor)
    actual_rpm = FloatField(clamped_rpm)
    slide_factor = FloatField(actual_rpm)
    rear_gear = IntegerField(40)
    gear = IntegerField(rear_gear)


class SceneVehicleCar(ByteStruct):
    is_update_async = BooleanField(offset=76)
    input_gas = FloatField(is_update_async)
    input_brake = FloatField(input_gas)
    input_steer = FloatField(input_brake)
    is_light_trials_set = BooleanField(116)
    horn_limit = IntegerField(148)
    quality = IntegerField(164)
    max_linear_speed = FloatField(736)
    gearbox_state = IntegerField(max_linear_speed)
    block_flags = IntegerField(gearbox_state)
    prev_sync_vehicle_state = StructField(block_flags, SceneVehicleCarState)
    sync_vehicle_state = StructField(block_flags, SceneVehicleCarState)
    async_vehicle_state = StructField(block_flags, SceneVehicleCarState)
    prev_async_vehicle_state = StructField(block_flags, SceneVehicleCarState)
    engine = StructField(1436, Engine)
    has_any_lateral_contact = BooleanField(1500)
    last_has_any_lateral_contact_time = IntegerField(has_any_lateral_contact)
    water_forces_applied = BooleanField(last_has_any_lateral_contact_time)
    turning_rate = FloatField(water_forces_applied)
    turbo_boost_factor = FloatField(1524)
    last_turbo_type_change_time = IntegerField(turbo_boost_factor)
    last_turbo_time = IntegerField(last_turbo_type_change_time)
    turbo_type = IntegerField(last_turbo_time)
    roulette_value = FloatField(1544)
    is_freewheeling = BooleanField(roulette_value)
    is_sliding = BooleanField(1576)
    wheel_contact_absorb_counter = IntegerField(1660)
    burnout_state = IntegerField(1692)
    current_local_speed = ArrayField(1804, shape=3, elem_field_type=FloatField)
    total_central_force_added = ArrayField(2072, shape=3, elem_field_type=FloatField)
    is_rubber_ball = BooleanField(2116)
    saved_state = ArrayField(is_rubber_ball, shape=(4, 3), elem_field_type=FloatField)


class SimStateData(ByteStruct):
    version = IntegerField(offset=0, signed=False)
    context_mode = IntegerField(offset=version, signed=False)
    flags = IntegerField(offset=context_mode, signed=False)
    timers = ArrayField(flags, shape=53, elem_field_type=IntegerField)
    dyna = StructField(timers, HmsDynaStruct)
    scene_mobil = StructField(dyna, SceneVehicleCar)
    simulation_wheels = ArrayField(scene_mobil, shape=4, elem_field_type=SimulationWheel)
    plug_solid = ByteArrayField(simulation_wheels, 68)
    cmd_buffer_core = ByteArrayField(plug_solid, 264)
    player_info = StructField(cmd_buffer_core, PlayerInfoStruct)
    internal_input_state = ArrayField(player_info, shape=10, elem_field_type=CachedInput)

    input_running_event = StructField(internal_input_state, InputEvent)
    input_finish_event = StructField(input_running_event, InputEvent)
    input_accelerate_event = StructField(input_finish_event, InputEvent)
    input_brake_event = StructField(input_accelerate_event, InputEvent)
    input_left_event = StructField(input_brake_event, InputEvent)
    input_right_event = StructField(input_left_event, InputEvent)
    input_steer_event = StructField(input_right_event, InputEvent)
    input_gas_event = StructField(input_steer_event, InputEvent)

    num_respawns = IntegerField(input_gas_event, signed=False)

    cp_data = StructField(num_respawns, CheckpointData)
