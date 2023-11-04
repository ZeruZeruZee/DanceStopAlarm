import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import os
import json
import time
import sys
from CreateAlarm import Ui_Dialog

from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import QFile,QTimer, QTime, QUrl
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect

import datetime

class CheckBoxGroup(QWidget):
	def __init__(self,data):
		super().__init__()
		layout = QHBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		self.setContentsMargins(0,0,0,0)
		i = 0

		self.checkbox = []
		for label in ["月", "火", "水", "木", "金", "土", "日"]:
			self.checkbox.append(QCheckBox(label))
			self.checkbox[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			self.checkbox[i].setChecked(data[i])
			layout.addWidget(self.checkbox[i])
			i += 1
		self.set_disabled(True)
		self.setLayout(layout)
	def set_disabled(self, is_disabled):
		for i in self.checkbox:
			i.setDisabled(is_disabled)

class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.setWindowTitle("新規アラームを作成")
		self.setWindowIcon(QIcon("icon_eye.jpg"))

		self.textbox = self.findChild(QLineEdit, "lineEdit")
		self.time = self.findChild(QTimeEdit, "timeEdit")
		self.song = self.findChild(QComboBox, "comboBox")
		self.check_loop = self.findChild(QCheckBox, "isLoop")
		self.slider = self.findChild(QSlider, "horizontalSlider")
		self.spinbox = self.findChild(QDoubleSpinBox, "doubleSpinBox")
		self.check_1 = self.findChild(QCheckBox, "checkBox_1")
		self.check_2 = self.findChild(QCheckBox, "checkBox_2")
		self.check_3 = self.findChild(QCheckBox, "checkBox_3")
		self.check_4 = self.findChild(QCheckBox, "checkBox_4")
		self.check_5 = self.findChild(QCheckBox, "checkBox_5")
		self.check_6 = self.findChild(QCheckBox, "checkBox_6")
		self.check_7 = self.findChild(QCheckBox, "checkBox_7")
		
		self.slider.setValue(80)
		self.spinbox.setValue(80)
		self.slider.valueChanged.connect(self.update_label_value)
		self.spinbox.valueChanged.connect(self.update_slider_value)

		self.set_disabled(True)
		self.check_loop.stateChanged.connect(self.checkbox_changed)

		self.song.addItems(load_songs())
		current_time = QTime.currentTime()
		current_time.setHMS(current_time.hour(), current_time.minute(), 0, 0)
		self.time.setTime(current_time)
	def update_label_value(self,value):
		self.spinbox.setValue(value)
	def update_slider_value(self,value):
		self.slider.setValue(value)
	def set_disabled(self, isDisabled):
		self.check_1.setDisabled(isDisabled)
		self.check_2.setDisabled(isDisabled)
		self.check_3.setDisabled(isDisabled)
		self.check_4.setDisabled(isDisabled)
		self.check_5.setDisabled(isDisabled)
		self.check_6.setDisabled(isDisabled)
		self.check_7.setDisabled(isDisabled)
	def checkbox_changed(self):
		if self.check_loop.isChecked():
			self.set_disabled(False)
		else:
			self.set_disabled(True)
	def getValue(self):
		result = []
		result.append(self.textbox.text())
		result.append(self.time.time())
		result.append(self.song.currentIndex())
		result.append(self.spinbox.value())
		result.append(self.check_loop.isChecked())
		result.append(self.check_1.isChecked())
		result.append(self.check_2.isChecked())
		result.append(self.check_3.isChecked())
		result.append(self.check_4.isChecked())
		result.append(self.check_5.isChecked())
		result.append(self.check_6.isChecked())
		result.append(self.check_7.isChecked())
		# テキストボックスの値を取得
		return result

class StartAlarm():
	def __init__(self,index,condition):
		self.load_ui("qt/Alarm.ui")
		self.song_path = self.get_path(index)
		self.window.setWindowTitle("アラーム")
		self.window.setWindowIcon(QIcon("icon_eye.jpg"))

		self.create_detector()
		self.load_jsonFile()
		self._danceLabel = self.window.findChild(QLabel, "dance_label")
		self._demoLabel  = self.window.findChild(QLabel, "demo_label" )
		self._scoreBar = self.window.findChild(QProgressBar, "score_bar")
		self._totalScoreLabel = self.window.findChild(QLabel, "totalScore_label")
		self._totalScoreBar = self.window.findChild(QProgressBar, "totalScore_bar")
		self._updateFlag = True
		self._demoIndex = 0
		self._now_timingList = self.json_data["timing"][self._demoIndex]
		self._condition = condition
		self.capture = cv2.VideoCapture(0)  # カメラのデフォルトデバイスを使用
		self.timer = QTimer()
		self.time = QTime()
		self._prev_time = self.time.currentTime()
		self._total_score = 0
		self._prev_total_score = 0
		self._max_score = 0
		self.effect = QSoundEffect()
		html_text = f"""
		<html><head/>
			<body>
				<p align="right">
				<span style=" font-size:20pt; font-weight:400;">クリア条件：</span>
				<span style=" font-size:28pt;">{condition}％</span>
				<span style=" font-size:20pt; font-weight:400;">以上</span>
				</p>
			</body>
		</html>
		"""

		self._totalScoreLabel.setText(html_text)
		song_path = self.song_path + "/song/song.wav"
		self.effect.setSource(QUrl.fromLocalFile(song_path))
		self.playSound()
		self.timer.timeout.connect(self.update_frame)
		self.timer.start(1000 // 30)  # 30 FPSで更新
	def playSound(self):
		self.effect.play()
		# start_cam(song_path)
	def load_demoImage(self, index):
		self._prev_total_score = self._total_score
		self._max_score = 0
		self._now_timingList = self.json_data["timing"][index]
		self._updateFlag = False
		self._prev_time = self.time.currentTime()

		demoImage_path = self.song_path + "/imgs"

		file_name = self._now_timingList["filename"]
		demoImage = cv2.imread(demoImage_path + "/" + file_name + ".jpg")
		mp_demoImage = mp.Image(image_format=mp.ImageFormat.SRGB, data=demoImage)

		self.original_demoImage	= mp_demoImage.numpy_view()
		self.result_demoDetection = self.pose_detector.detect(mp_demoImage)
		self.result_demoDetection_face = self.face_detector.detect(mp_demoImage)

		return mp_demoImage
	def restart(self):
		self._total_score = 0
		self._prev_total_score = 0
		self.playSound()
		self._demoIndex = 0
		self._updateFlag = True
	def stop(self):
		self.window.close()
	def update_frame(self):
		ret, frame = self.capture.read()

		if ret:
			now_time = self.time.currentTime()
			time_interval = self._prev_time.msecsTo(now_time)

			interval_msecs = (self.beat_interval * self._now_timingList["interval"]) * 1000
			# print([self._demoIndex,len(self.json_data["timing"]),interval_msecs])
			if time_interval >= interval_msecs:
				if self._demoIndex+1 >= len(self.json_data["timing"]):
					percentage_score = self._total_score / (len(self.json_data["timing"]) - 1)
					if self._condition <= percentage_score:
						self.stop()
					else:
						self.restart()
				else:
					self._updateFlag = True
					self._demoIndex += 1
			if self._updateFlag:
				self.load_demoImage(self._demoIndex)
			# 左右反転
			frame = cv2.flip(frame, 1)
			height, width, _ = frame.shape
			bytes_per_line = 3 * width

			mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
			original_image = mp_image.numpy_view()

			result_detection = self.pose_detector.detect(mp_image)
			result_detection_face = self.face_detector.detect(mp_image)
			annotated_image = original_image
			annotated_image = draw_face_icon(annotated_image, result_detection_face,result_detection, frame.shape, "icon.jpg")
			annotated_image = draw_landmarks(annotated_image, result_detection)
			# annotated_image = draw_angle(annotated_image, result_detection, frame.shape)

			annotated_demoImage = self.original_demoImage
			annotated_demoImage = draw_landmarks(annotated_demoImage, self.result_demoDetection)
			annotated_demoImage = draw_face_icon(annotated_demoImage, self.result_demoDetection_face,self.result_demoDetection, frame.shape,"icon_demo.jpg")
			
			annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
			annotated_demoImage = cv2.cvtColor(annotated_demoImage, cv2.COLOR_BGR2RGB)

		if(self._demoIndex < len(self.json_data["timing"]) - 1):
			score = pose_similarity(result_detection, self.result_demoDetection)
			self._scoreBar.setValue(score)
			if score >= self._max_score:
				self._max_score = score
				self._total_score = self._prev_total_score + self._max_score
				percentage_score = self._total_score / (len(self.json_data["timing"]) - 1)
				self._totalScoreBar.setValue(percentage_score)
			# print(QTime.currentTime())
			
			def getPixmap(image):
				q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
				pixmap = QPixmap.fromImage(q_image)
				return pixmap
			
			self._danceLabel.setPixmap(getPixmap(annotated_image))
			self._demoLabel.setPixmap(getPixmap(annotated_demoImage))
	def create_detector(self):
		# PoseLandmarkerオブジェクトを作成
		pose_options = vision.PoseLandmarkerOptions(
			base_options=python.BaseOptions(model_asset_path='pose_landmarker_lite.task'),
			output_segmentation_masks=True
		)

		# FaceDetectorオブジェクトを作成
		face_options = vision.FaceDetectorOptions(
			base_options = python.BaseOptions(model_asset_path = 'blaze_face_short_range.tflite'),
		)

		self.pose_detector = vision.PoseLandmarker.create_from_options(pose_options)
		self.face_detector = vision.FaceDetector.create_from_options(face_options)
		self.start_flag = True
	def load_jsonFile(self):
		json_file = open(self.song_path + "/data.json", "r", encoding="utf-8")
	
		self.json_data = json.load(json_file)
		json_bpm  = self.json_data["bpm"]
		self.json_timing = self.json_data["timing"]

		self.beat_interval = 60 / json_bpm
	def get_path(self,index):
		directory_path = "songData"

		file_list = os.listdir(directory_path)
		first_file = file_list[index]
		relative_path = os.path.join(directory_path, first_file)
		return relative_path
	def load_ui(self,mainwindow_file_path):

		ui_file = QFile(mainwindow_file_path)
		ui_file.open(QFile.ReadOnly)
		
		loader = QUiLoader()
		self.window = loader.load(ui_file)
		self.window.move(100,50)
		ui_file.close()

class MainWindow:
	def __init__(self, mainwindow_file_path):
		self.load_ui(mainwindow_file_path)
		self.window.setWindowTitle("アラーム一覧")
		self.window.setWindowIcon(QIcon("icon_eye.jpg"))

		self._tableWidget = self.window.findChild(QTableWidget, "tableWidget")
		self._addButton = self.window.findChild(QPushButton, "button_add")
		self._nowTime = self.window.findChild(QLabel, "label")
		self._idList = []

		self.timer = QTimer()
		self.timer.timeout.connect(self.update_time)
		self.timer.start(1000)  # Update every 1000 ms (1 second)

		self.set_table()
		self.set_button()
	def update_time(self):
		current_time = QTime.currentTime()
		# 現在の日付を取得
		today = datetime.date.today()

		# 曜日を取得 (0: 月曜日, 1: 火曜日, 2: 水曜日, 3: 木曜日, 4: 金曜日, 5: 土曜日, 6: 日曜日)
		weekday = today.weekday()
		# print(weekday)

		# ミリ秒を0に設定
		current_time.setHMS(current_time.hour(), current_time.minute(), current_time.second(), 0)

		display_text = current_time.toString("hh:mm")
		self._nowTime.setText(display_text)
		isEnabled = False
		widget_songIndex = 0
		widget_condition = 0
		for row in range(self._tableWidget.rowCount()):
			widgetTime = self._tableWidget.cellWidget(row, 2).time()
			widget_enableCheck = self._tableWidget.cellWidget(row, 0).isChecked()

			widget_loopCheck = self._tableWidget.cellWidget(row, 5).isChecked()
			widget_dateCheckGroup = self._tableWidget.cellWidget(row, 6)
			today_check = widget_dateCheckGroup.checkbox[weekday].isChecked()
			
			if (widgetTime is not None) and (widgetTime == current_time) and (widget_enableCheck):
				if widget_loopCheck:
					if today_check:
						widget_songIndex = self._tableWidget.cellWidget(row, 3).currentIndex()
						widget_condition = self._tableWidget.cellWidget(row, 4).value()
						isEnabled = True
				else:
					widget_songIndex = self._tableWidget.cellWidget(row, 3).currentIndex()
					widget_condition = self._tableWidget.cellWidget(row, 4).value()
					isEnabled = True
					self._tableWidget.cellWidget(row, 0).setChecked(False)
		if isEnabled:
			self.alarm_window = StartAlarm(widget_songIndex, widget_condition)
			self.alarm_window.window.show()

				#column_items.append(cell_text)
	def load_ui(self,mainwindow_file_path):
		ui_file = QFile(mainwindow_file_path)
		ui_file.open(QFile.ReadOnly)

		loader = QUiLoader()
		self.window = loader.load(ui_file)
		ui_file.close()
	def set_button(self):
		self._addButton.clicked.connect(lambda: self.createAlarm())
	def set_table(self):
		self._tableWidget.horizontalHeader().hide()
		self._tableWidget.verticalHeader().hide()
		
		headertitle = ("enable","name","time","song","condition","loop","date", "delete")
		self._tableWidget.setColumnCount(8)
		self._tableWidget.setHorizontalHeaderLabels(headertitle)
		#self._tableWidget.insertLine(0)
		self._tableWidget.removeRow(0)

		# ダブルクリックで編集可能に
		# self._tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)

		# 行で選択できるように
		self._tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

		# ヘッダーをウィンドウサイズに合わせて変形
		header = self._tableWidget.horizontalHeader()
		self._tableWidget.setColumnWidth(0, 60)
		self._tableWidget.setColumnWidth(1, 300)
		self._tableWidget.setColumnWidth(2, 100)
		self._tableWidget.setColumnWidth(3, 150)
		self._tableWidget.setColumnWidth(4, 70)
		self._tableWidget.setColumnWidth(5, 80)
		self._tableWidget.setColumnWidth(6, 300)
		header.setSectionResizeMode(1, QHeaderView.Stretch)

		# 最大サイズを設定
		#self._tableWidget.setColumnWidth(1,1)
	def createAlarm(self):
		dialog = CustomDialog()
		result = dialog.exec()

		if result == QDialog.Accepted:
			alarm_data = dialog.getValue()
			self.add_line(alarm_data)
	def add_line(self,alarm_data):
		index = self._tableWidget.rowCount()
		self._tableWidget.insertRow(index)

		id = 0
		sorted_id = sorted(self._idList)
		for id in range(len(sorted_id)):
			if id != sorted_id[id]:
				break
			if id == len(sorted_id) - 1:
				id += 1


		self._idList.append(id)

		enableCheckBox = QCheckBox()
		enableCheckBox.setText("有効")
		enableCheckBox.setChecked(True)

		alarmName = QLineEdit()
		alarmName.setText(alarm_data[0])

		timeEdit = QTimeEdit()
		timeEdit.setTime(alarm_data[1])

		songSelector = QComboBox()
		songSelector.addItems(load_songs())
		songSelector.setCurrentIndex(alarm_data[2])

		conditionBox = QDoubleSpinBox()
		conditionBox.setValue(alarm_data[3])

		loopCheckBox = QCheckBox()
		loopCheckBox.setText("繰り返す")
		loopCheckBox.setChecked(alarm_data[4])

		loopDate = CheckBoxGroup(alarm_data[5:12])
		loopCheckBox.stateChanged.connect(lambda:change_loop())
		def change_loop():
			CheckBoxGroup.set_disabled(loopDate,not loopCheckBox.isChecked())

		delButton = QPushButton()
		delButton.setText("delete")
		delButton.clicked.connect(lambda : self.delete_line(id))
		#loopDate.setText("曜日を選択")


		widget = [
			enableCheckBox,
			alarmName,
			timeEdit,
			songSelector,
			conditionBox,
			loopCheckBox,
			loopDate,
			delButton
		]

		self._tableWidget.setCellWidget(index, 0, widget[0])
		self._tableWidget.setCellWidget(index, 1, widget[1])
		self._tableWidget.setCellWidget(index, 2, widget[2])
		self._tableWidget.setCellWidget(index, 3, widget[3])
		self._tableWidget.setCellWidget(index, 4, widget[4])
		self._tableWidget.setCellWidget(index, 5, widget[5])
		self._tableWidget.setCellWidget(index, 6, widget[6])
		self._tableWidget.setCellWidget(index, 7, widget[7])
		#self._tableWidget.setItem(index, 5, item)
	def delete_line(self, id):
		index = 0
		for index in range(len(self._idList)):
			if self._idList[index] == id:
				break
		del self._idList[index]

		self._tableWidget.removeRow(index)

def draw_landmarks(rgb_image, detection_result):
	pose_landmarks_list = detection_result.pose_landmarks
	annotated_image = np.copy(rgb_image)

	for idx in range(len(pose_landmarks_list)):
		pose_landmarks = pose_landmarks_list[idx]

		pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
		pose_landmarks_proto.landmark.extend([
			landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
		])
		solutions.drawing_utils.draw_landmarks(
			annotated_image,
			pose_landmarks_proto,
			solutions.pose.POSE_CONNECTIONS,
			solutions.drawing_styles.get_default_pose_landmarks_style())
	return annotated_image

def draw_face_icon(rgb_image, detection_result,landmark_result, frame_shape,icon_name):
	annotated_image = np.copy(rgb_image)

	detections_list = detection_result.detections
	landmarks_list = landmark_result.pose_landmarks
	
	frame_height, frame_width, _ = frame_shape
	icon_size = (100,100)
	# icon.jpgの読み込み
	icon_image = cv2.imread(icon_name, cv2.IMREAD_UNCHANGED)

	isDetected = False
	# icon_imageをframeと同じサイズにリサイズ
	icon_image = cv2.resize(icon_image, icon_size)

	# 姿勢検出の結果からアイコンを配置 
	if (len(landmarks_list) > 0):
		landmark = landmarks_list[0]
		face_center_x = int(frame_width * (landmark[0].x))
		face_center_y = int(frame_height * (landmark[0].y))
		isDetected = True

	# 顔検出の結果からアイコンを配置
	elif (len(detections_list) > 0):
		detection = detections_list[0]
		keypoints_nose = detection.keypoints[2]

		face_center_x = int(frame_width * (keypoints_nose.x))
		face_center_y = int(frame_height * (keypoints_nose.y))
		isDetected = True

	# アイコンを描画 
	if isDetected:
		# icon_height, icon_width = icon_image.shape
		x_start = int(face_center_x - (icon_size[0] / 2))
		x_end 	= int(face_center_x + (icon_size[0] / 2))
		y_start	= int(face_center_y - (icon_size[1] / 2))
		y_end 	= int(face_center_y + (icon_size[1] / 2))

		i_x_start	= 0
		i_x_end 	= icon_size[1]
		i_y_start	= 0
		i_y_end 	= icon_size[0]

		if x_start < 0:
			i_x_start = 0 - x_start
			x_start = 0
		if y_start < 0:
			i_y_start = 0 - y_start
			y_start = 0
		if x_start > frame_width:
			i_x_start = frame_width - x_start
			x_start = frame_width
		if y_start > frame_height:
			i_y_start = frame_height - y_start
			y_start = frame_height
		annotated_image[y_start:y_end, x_start:x_end] = icon_image[i_y_start:i_y_end, i_x_start:i_x_end]
			# annotated_image[y_start:y_start+icon_height, x_start:x_start+icon_width, c] = icon_image[:, :, c]

	# 顔が検出されなかった場合はぼかす
	else:
		annotated_image = cv2.GaussianBlur(annotated_image, (101, 101), 0)
	return annotated_image

def calculate_angle(point_a,point_b,point_c):
	np_a = np.array([point_a.x, point_a.y, point_a.z])
	np_b = np.array([point_b.x, point_b.y, point_b.z])
	np_c = np.array([point_c.x, point_c.y, point_c.z])
	vector_ab = np_b - np_a
	vector_bc = np_c - np_b
	# 内積の計算
	dot_product = np.dot(vector_ab, vector_bc)
	
	# 大きさを計算
	magnitude_ab = np.linalg.norm(vector_ab)
	magnitude_bc = np.linalg.norm(vector_bc)
	
	# 角度の計算
	cosine_angle = dot_product / (magnitude_ab * magnitude_bc)
	angle_in_radians = np.arccos(cosine_angle)
	
	# ラジアンから度に変換
	angle_in_degrees = np.degrees(angle_in_radians)

	return (angle_in_radians / math.pi)*100

def pose_similarity(pose1, pose2):
	if len(pose1.pose_landmarks) == 0 or len(pose2.pose_landmarks) == 0:
		# 姿勢が見つからない場合はスコアは0
		return 0

	landmarks_1 = pose1.pose_landmarks[0]
	landmarks_2 = pose2.pose_landmarks[0]

	hinge_keypoints = np.array((
		(16	,14	,12	),
		(14	,12	,24	),
		(24	,26	,28	),
		(23	,24	,26	),

		(15	,13	,11	),
		(13	,11	,23	),
		(23	,25	,27	),
		(24	,23	,25	)
	))

	sum_angle = 0

	for hinge in hinge_keypoints:
		index_a,index_b,index_c = hinge[0], hinge[1], hinge[2]
		angle_1 = calculate_angle(landmarks_1[index_a],landmarks_1[index_b],landmarks_1[index_c])
		angle_2 = calculate_angle(landmarks_2[index_a],landmarks_2[index_b],landmarks_2[index_c])
		sum_angle += abs(angle_1 - angle_2)
	ave_angle = sum_angle / len(hinge_keypoints)
	score = 100 - ave_angle

	# cv2.putText(annotated_1, "angle_1",(200,200) , cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 0))
	return score

def start_cam(song_path):
	# PoseLandmarkerオブジェクトを作成
	pose_options = vision.PoseLandmarkerOptions(
		base_options=python.BaseOptions(model_asset_path='pose_landmarker_lite.task'),
		output_segmentation_masks=True
	)
	pose_detector = vision.PoseLandmarker.create_from_options(pose_options)
	
	# FaceDetectorオブジェクトを作成
	face_options = vision.FaceDetectorOptions(
		base_options = python.BaseOptions(model_asset_path = 'blaze_face_short_range.tflite'),
	)
	face_detector = vision.FaceDetector.create_from_options(face_options)

	json_file = open(song_path + "/data.json", "r", encoding="utf-8")
	
	json_data = json.load(json_file)
	json_bpm = json_data["bpm"]
	json_beat = json_data["beat"]
	beat_interval = (60 / json_bpm) * json_beat

	demoImage_path = song_path + "/imgs"
	demoImage_list = os.listdir(demoImage_path)

	demoImage = cv2.imread(demoImage_path + "/" + demoImage_list[0])
	mp_demoImage = mp.Image(image_format=mp.ImageFormat.SRGB, data=demoImage)
	original_demoImage	= mp_demoImage.numpy_view()
	result_demoDetection = pose_detector.detect(mp_demoImage)
	result_demoDetection_face = face_detector.detect(mp_demoImage)

	cap = cv2.VideoCapture(0)
	start_time = time.time()
	prev_time = start_time
	demoImage_index = 0
	while cap.isOpened():
	# while False:
		ret, frame = cap.read()
		frame = cv2.flip(frame, 1)# 左右反転

		now_time = time.time()

		# demoImageを更新
		if(now_time - prev_time >= beat_interval):
			prev_time = prev_time + beat_interval
			demoImage_index += 1
			if(demoImage_index >= len(demoImage_list)):
				demoImage_index = 0
			demoImage = cv2.imread(demoImage_path + "/" + demoImage_list[demoImage_index])
			mp_demoImage = mp.Image(image_format=mp.ImageFormat.SRGB, data=demoImage)
			original_demoImage	= mp_demoImage.numpy_view()
			result_demoDetection = pose_detector.detect(mp_demoImage)
			result_demoDetection_face = face_detector.detect(mp_demoImage)


		mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
		original_image = mp_image.numpy_view()

		result_detection = pose_detector.detect(mp_image)
		result_detection_face = face_detector.detect(mp_image)
		annotated_image = original_image
		annotated_image = draw_face_icon(annotated_image, result_detection_face,result_detection, frame.shape, "icon.jpg")
		annotated_image = draw_landmarks(annotated_image, result_detection)
		# annotated_image = draw_angle(annotated_image, result_detection, frame.shape)
		
		annotated_demoImage = original_demoImage
		annotated_demoImage = draw_landmarks(annotated_demoImage, result_demoDetection)
		annotated_demoImage = draw_face_icon(annotated_demoImage, result_demoDetection_face,result_demoDetection, frame.shape,"icon_demo.jpg")
		annotated_image = pose_similarity(
			result_detection, result_demoDetection, annotated_image, frame.shape
		)
		# ax.cla()
		# plt_landmarks(result_demoDetection)
		# plt_landmarks(result_detection)
		# plt.pause(0.1)
		# cv2.imshow("Video", video_frame)
		cv2.imshow("demo", cv2.cvtColor(annotated_demoImage, cv2.COLOR_RGB2RGBA))
		cv2.imshow("pose landmark", cv2.cvtColor(annotated_image, cv2.COLOR_RGB2RGBA))

		# 'q'キーでループを終了
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

def load_songs():
	directory_path = "songData"
	songs_list = []
	file_list = os.listdir(directory_path)
	for i_fileName in file_list:
		relative_path = os.path.join(directory_path, i_fileName)
		json_file = open(relative_path + "/data.json", "r", encoding="utf-8")
		json_data = json.load(json_file)
		json_singTitle = json_data["title"]
		songs_list.append(json_singTitle)
	return songs_list

def main():
	# song_path = select_song()
	# start_cam(song_path)
	
	app = QApplication(sys.argv)
	mainWindow_path = "qt/MainWindow_tableWidget.ui"

	main_window = MainWindow(mainWindow_path)
	main_window.window.show()
	# alarm_window = StartAlarm(0,90)
	# alarm_window.window.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()