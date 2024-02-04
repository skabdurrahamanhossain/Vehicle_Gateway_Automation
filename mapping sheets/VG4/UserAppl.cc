
//------------------------------------------------------------------------------------------//
//   Company				:Continental Automotive India Pvt. Ltd. (Bangalore)
//   Project				:VG4 Open Loop Gateway
//   Filename				:UserAppl.cc
//   Created By				:Hossain, SK Abdur Rahaman (uif74893)
//------------------------------------------------------------------------------------------//
//   Gateway Software Developers    :
//				JaRa                :		Jayapandiyan Ramu (BLN)
//				ABRA                :		Abdur Rahaman (BLN)
//------------------------------------------------------------------------------------------//
//   Created On:		:
//		Date				:12/11/2023
//		Time				:11:13:28 AM
//------------------------------------------------------------------------------------------//
//   Version History					:
//
//   Hossain, SK Abdur Rahaman (uif74893)       : v 1.0.0: initial revision
//------------------------------------------------------------------------------------------//


#include "UserAppl.h"
//#include "../Driver/EthProtocoll/EthSocket.h"
#pragma ghs section text =" .User "

CDispatchLoop DispatchLoop;

enum{Timer1ms_0=0};
enum{Can_0=0,Can_1,Can_2,Can_3,Can_4,Can_5};

//Channel Allocation
CCan	C-HRCAN(Can_0,500000);
CCan	SRR320SU16CAN(Can_1,500000);

//Objects
CC-HR		C-HRObject(&C-HRCAN);
CSRR320SU16		SRR320SU16Object(&SRR320SU16CAN);

//Serial communication
//CSerio  SerioDISPLAY(DISPLAY_UART,115200);
CSerio  SerioUSB(USB_UART,115200);
CSerio  SerioRS232(RS232_UART,115200);

CVersion Version(&SerioUSB);
CTimerAUD Timer(0);

void initValues(){
	Version.setVersion(1,0,0);
	Version.setFahrzeug("C-HR_SRR320SU16");
	Version.setProjekt("VG4_C-HR_SRR320SU16");
	Version.setPlattform(0,"C-HR");
	Version.setPlattform(1,"SRR320SU16");
	Version.setCanDesc(0,"C-HR");
	Version.setCanDesc(1,"SRR320SU16");
	Version.setComent("VG4 Open LoopGateway ");
}

void CDispatchLoop::dispatchEvent(CEvent event) {

	switch(event.type) {
	case Ev_System: {
		switch(event.subtype) {
		case Ev_System_Init: {
			initValues();
			//SerioDISPLAY.start();
			SerioUSB.start();
			SerioRS232.start();
			//Flex.setMsgData(m_VectorList);
			//Flex.setIrqs(0x00000001, 0x00000004);//don't change
			C-HRCAN.start();
			SRR320SU16CAN.start();
			//Can2.start();
			//Can3.start();
			//Can4.start();
			//Can5.start();
			Timer.repeat(1000);

			} break; // Ev_System
		case Ev_System_Err: {
			//Error Event
			} break;
		} // event.subtype
	} break; // case
	case Ev_Can : {
		switch(event.subtype) {
		case Ev_Can_Rx: {
			CCanMsg rxMsg;
			switch (event.channel){
				case Can_0:{//Can0
					C-HRCAN.receive(&rxMsg);
					C-HRObject.receive(&rxMsg);
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_6_4_REVERSE_MT = 0;
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_7_0_HEADLAMP_SMALL = 0;
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_2_3_CSTM_WGN_SDN = 0;
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_5_4_DIMMER_CANCEL = 0;
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.BIU3AC.BIU3AC_6_7_TOWING_SW = 0;
							SRR320SU16Object.m_PhysTx.EGI040.EGI040_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.EGI040.EGI040_1_7_REPROGRAMING = 0;
							SRR320SU16Object.m_PhysTx.EGI040.EGI040_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.ISS174.ISS174_2_5_STATE_VOLT_DROP = 0;
							SRR320SU16Object.m_PhysTx.ISS174.ISS174_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.ISS174.ISS174_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.MET390.MET390_1_0_MSG_COUNTER = ;
							SRR320SU16Object.m_PhysTx.MET390.MET390_2_0_VEHICLE_SERIES = 5;
							SRR320SU16Object.m_PhysTx.MET390.MET390_2_3_DESTINATION = 1;
							SRR320SU16Object.m_PhysTx.MET390.MET390_6_4_BRIGHT_SW = 1;
							SRR320SU16Object.m_PhysTx.MET390.MET390_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.TCU048.TCU048_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.TCU048.TCU048_1_6_STATUS_TCM = 1;
							SRR320SU16Object.m_PhysTx.TCU048.TCU048_1_7_REPROGRAMING = 0;
							SRR320SU16Object.m_PhysTx.TCU048.TCU048_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.VDC138.VDC138_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.VDC138.VDC138_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.VDC139.VDC139_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.VDC139.VDC139_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.VDC139.VDC139_1_5_VEHICLE_HIGHT = 2;
							SRR320SU16Object.m_PhysTx.VDC139.VDC139_1_7_REPROGRAMING = 0;
							SRR320SU16Object.m_PhysTx.VDC328.VDC328_2_1_WARN_ABS_MET_LCD = 0;
							SRR320SU16Object.m_PhysTx.VDC328.VDC328_0_0_CHECK_SUM = 0;
							SRR320SU16Object.m_PhysTx.VDC328.VDC328_1_0_MSG_COUNTER = 0;
							SRR320SU16Object.m_PhysTx.VDC328.VDC328_2_2_WARN_VDC_MET_LCD = 0;
					switch(rxMsg.id) {
						case BDB1F03_C-HR_ID : {			//ID:0x63B
							SRR320SU16Object.m_PhysTx.BIU660.BIU660_3_0_COUNT_TRIP = C-HRObject.m_PhysRx.BDB1F03.TRIP_CNT;
						} break;
						case MET1S10_C-HR_ID : {			//ID:0x614
							SRR320SU16Object.m_PhysTx.MET390.MET390_6_2_TURN_SIG_LEFT = C-HRObject.m_PhysRx.MET1S10.TNS;
						} break;
						case ECT1S92_C-HR_ID : {			//ID:0x3BC
							SRR320SU16Object.m_PhysTx.TCU048.TCU048_3_0_IND_SHIFT_POS = C-HRObject.m_PhysRx.ECT1S92.Refer Gear Pos sheet;
						} break;
						case STR1S01_C-HR_ID : {			//ID:0x25
							SRR320SU16Object.m_PhysTx.VDC138.VDC138_2_0_STEER_ANGLE = C-HRObject.m_PhysRx.STR1S01.SSA*;
						} break;
						case YGS1S03_C-HR_ID : {			//ID:0x24
							SRR320SU16Object.m_PhysTx.VDC138.VDC138_4_0_YAW_RATE = C-HRObject.m_PhysRx.YGS1S03.YR*0.017453292519943295;
						} break;
						case VSC1F01_C-HR_ID : {			//ID:0x0AA
							SRR320SU16Object.m_PhysTx.VDC139.VDC139_2_0_SPD_WHEEL_AVE = C-HRObject.m_PhysRx.VSC1F01.VXFR;
						} break;
						default: {      } break;
					}; // msg.id
				}break;//Can0
				case Can_1:{//Can1
				}break;//Can1
			};//event.channel
		} break; // Can Rx
	}break; // Ev_Can
	case Ev_Timer :{
		switch (event.channel){ //check timer number
			case Timer1ms_0:{
				C-HRObject.tick1ms(event.user);
				SRR320SU16Object.tick1ms(event.user);

				if (!(event.user % 500)){
				LED_0 = ~LED_0;}
			}break;
		}
	}break;//Timer
	case Ev_Uart:{
		if (event.subtype==Ev_Uart_Rx)
			switch(event.channel){
				case USB_UART:{
					char string[255];
					SerioUSB.getString(string,255);
					if (strcmp(string,"Version")==0)Version.sendVersion();
					if (strcmp(string,"Reset")==0)swReset();
				}break;
			}
		}break;
	} break;//UART
	default: {}break;

	} // switch
} // CanLoop::DispatchEvent()
//------------------------------------------------------------------------------------------//
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
	                                   
