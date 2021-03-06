#include <openvr.h>
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <algorithm>

#define NOMINMAX
#include <winsock2.h>

#include "SerialClass.h"

#define APPLE_PI 3.14159265359
#define HALF_PI 1.57079633
#define HALF_PI_3 4.71238899
#define RAD_TO_DEG 57.295779513082320876798154814105
#define DEG_TO_RAD 0.017453292519943295769236907684886
#define degrees(rad) ((rad)*RAD_TO_DEG)
#define radians(deg) ((deg)*DEG_TO_RAD)

using namespace vr;

struct ViveDevice {
	enum DeviceName {
		HMD,
		Right,
		Left,

		Wrong
	};

	DeviceName name;

	HmdVector3_t XYZ;
	HmdQuaternion_t ROT;

	bool valid;
	ETrackingResult trackingResult;

	void setPosAndRot(HmdVector3_t p, HmdQuaternion_t r);

	char* getEnglishPoseValidity();
	char* getEnglishTrackingResultForPose();
	char* print();

	ViveDevice(char name);
};

struct ViveController : ViveDevice {
	float dPadX;
	float dPadY;
	float trigger;

	HmdVector3_t relativeXYZ;
	HmdQuaternion_t relativeROT;

	bool calibarated = false;

	void setInputs(float dx, float dy, float t);
	char* print(bool rel);

	ViveController(char name) : ViveDevice(name) {
		dPadX = 0;
		dPadY = 0;
		trigger = 0;
		relativeXYZ = HmdVector3_t();
		relativeROT = HmdQuaternion_t();
	};
};

enum HumanName {
	Albert,
	Paulina,
	Sam,
	John
};

struct Human {
	float armLength;
	float headToArmAcross;

	HmdVector3_t shoulderPos;
	HmdVector3_t headShoulderDistance;

	void calcHeadShoulderOffset(ViveController con, ViveDevice H);

	Human(HumanName n);
};

struct AllViveDevices {
	ViveDevice H = ViveDevice('H');
	ViveController R = ViveController('R');
	ViveController L = ViveController('L');

	void calcRelHandPos(Human Hu);
	void print(bool rel);
};

struct RobotArm {
	float upperArmLength;
	float foreArmLength;
	float handLength;

	float upperArmLenSq, foreArmLenSq, handLenSq;

	HmdVector3_t handPosition;

	float armMaxLength;
	float human2ArmConversion;

	float baseAngle = 90;
	float shoulderAngle = 90;
	float elbowAngle = 90;
	float wristAngle = 90;

	int gripAngle = 0;

	Serial* SP;

	bool ONLINE;
	WSADATA wsaData;
	SOCKET server = INVALID_SOCKET;
	SOCKADDR_IN addr;

	void calcHandPosition(ViveController C);
	void calcAngles(ViveController C);
	void inverseKin();

	bool sendAngles(int base, int shoulder, int elbow, int wrist, int grip);

	RobotArm(float humanArmLength, float ul, float fl, float hl, const char* serial_port, bool online);
	virtual ~RobotArm();
};
