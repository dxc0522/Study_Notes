const fs = require("fs");
const dirName = titleCase(process.argv[2]);

if (!dirName) {
    console.error("页面或模块名称不能为空");
    process.exit(0);
}

const genType = (process.argv[3]).toLowerCase();
if (genType !== "p" && genType !== "c") {
    console.error("生成类型不能为空");
    process.exit(0);
}

// 页面文件模版
const pageTpl = `
import Taro, { Component, Config } from '@tarojs/taro'
import { View } from '@tarojs/components'
import { ComponentClass } from 'react'
import './index.scss'
import { connect } from '@tarojs/redux'

type PageStateProps = {
  counter: any
}
type PageDispatchProps = {
}
type PageOwnProps = {
}
type PageState = {
}
type IProps = PageStateProps & PageDispatchProps & PageOwnProps

interface ${dirName} {
  props: IProps;
  state: PageState
}
@connect(({ counter }) => ({
  counter
}), (dispatch) => ({

}))
class ${dirName} extends Component {
  config: Config = {
    navigationBarTitleText: '${dirName}'
  }
  state = {

  }
  componentDidMount() {
    
  }
  render() {
    const { } = this.state;
    const { } = this.props.counter;
    return (
      <View>
      ${dirName}
      </View >
    )
  }
}
export default ${dirName} as ComponentClass<PageOwnProps, PageState>
`;

// 组件文件模版
const compTpl = `
import Taro, { Component, Config, ComponentOptions } from '@tarojs/taro'
import { View } from '@tarojs/components'
import { ComponentClass } from 'react'
import './index.scss'
import { connect } from '@tarojs/redux'

type PageStateProps = {
  counter: any
}
type PageDispatchProps = {
}
type PageOwnProps = {
}
type PageState = {
}
type IProps = PageStateProps & PageDispatchProps & PageOwnProps

interface ${dirName} {
  props: IProps;
  state: PageState
}
@connect(({ counter }) => ({
  counter
}), (dispatch) => ({

}))
class ${dirName} extends Component {
  static config: Config = {
    navigationBarTitleText: '${dirName}'
  }
  static options: ComponentOptions = {
    "addGlobalClass": true
  }
  state = {

  }
  componentDidMount() {
    
  }
  render() {
    const { } = this.state;
    const { } = this.props.counter;
    return (
      <View>
      ${dirName}
      </View >
    )
  }
}
export default ${dirName} as ComponentClass<PageOwnProps, PageState>

`;

let parentDir = process.argv[4];
let boo = false;
if (parentDir) {
    parentDir = titleCase(parentDir);
    boo = true;
}

// 创建页面
if (genType === "p") {
    if (boo) {
        if (!fs.existsSync(`./src/pages/${parentDir}`)) {
            fs.mkdirSync(`./src/pages/${parentDir}`);
        }
        fs.mkdirSync(`./src/pages/${parentDir}/${dirName}`);
        process.chdir(`./src/pages/${parentDir}/${dirName}`);
    } else {
        fs.mkdirSync(`./src/pages/${dirName}`);
        process.chdir(`./src/pages/${dirName}`);
    }

    fs.writeFileSync('Index.tsx', pageTpl);
    fs.writeFileSync('Index.scss', '');
}

// 创建组件
if (genType === "c") {
    if (boo) {
        if (!fs.existsSync(`./src/Components/${parentDir}`)) {
            fs.mkdirSync(`./src/Components/${parentDir}`);
        }
        fs.mkdirSync(`./src/Components/${parentDir}/${dirName}`);
        process.chdir(`./src/Components/${parentDir}/${dirName}`);
    } else {
        fs.mkdirSync(`./src/Components/${dirName}`);
        process.chdir(`./src/Components/${dirName}`);
    }

    fs.writeFileSync('Index.tsx', compTpl);
    fs.writeFileSync('Index.scss', '');
}

console.log(`模版${dirName}已创建,请手动至app.tsx文件添加页面路径`);

function titleCase(str) {
    const first = str[0];
    const string = first.toUpperCase() + str.substr(1);
    return string;
}

function insertStr(soure, newStr, start) {
    return soure.slice(0, start) + newStr + soure.slice(start)
}

process.exit(0);